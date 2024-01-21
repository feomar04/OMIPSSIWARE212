# Projet Malware Omar Fegousse MCS LYN

Ce s'agit d'un programme client(victime)/serveur(pirate) permettant d'interagir avec un système distant et effectuer des actions malveillante . Le projet a été conçu pour illustrer divers concepts de création des malwares.

## Fonctionnalités

1. **Reverse Shell :** La fonctionnalité de shell inversé permet au serveur de se connecter à la ligne de commande du client distant et d'exécuter des commandes à distance.

2. **Lister les Fichiers :** Le serveur peut demander au client de lister les fichiers présents dans le répertoire courant.

3. **Chiffrer les Fichiers :** Le serveur peut demander au client de chiffrer les fichiers du système distant à l'aide d'une clé , et l'affichage d'une fenetre au niveau client qui informe la victime que les fichiers sont cryptés et qu'il doit contacter le pirate a travers un email mentionné pour le decryptage. 
 
4. **Déchiffrer les Fichiers :** Le serveur peut demander au client de déchiffrer les fichiers chiffrés précédemment,  et l'affichage d'une fenetre au niveau de la victime pour lui informer que les fichiers sont decryptés . 

5. **Activer le Keylogger :** Le serveur peut activer un keylogger sur le client pour capturer les frappes de clavier et envoyer les données vers la machine serveur.

## Les Dangers Potentiels

1. **Violation de la Vie Privée :** Un keylogger peut enregistrer des informations sensibles, violant la vie privée des utilisateurs de la machine cliente.

2. **Dommages aux Fichiers :** Les fonctionnalités de chiffrement et de déchiffrement peuvent potentiellement causer des dommages permanents aux fichiers de la machine cliente.

3. **Accès Non Autorisé :** Un shell inversé peut être utilisé pour exécuter des commandes sur la machine cliente sans le consentement de l'utilisateur, représentant une menace pour la sécurité.

## Instructions d'utilisation

1. **Configuration du Serveur :** L'éxécution du script serveur.py sur la machine qui agira comme le serveur.
   python serveur.py
   
2. **Configuration du Client :** L'éxécution du script client.py au niveau de la machine victime d'une manière anonyme ce qui permet son espionnage .
  
3. **Choix des Actions :** Le serveur affichera un menu permettant de choisir différentes actions à effectuer sur le client distant.
   
4. **Sortie :** Pour quitter proprement, utilisez l'option 'exit'.
