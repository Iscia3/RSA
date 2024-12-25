#!/usr/bin/env python3

import socket
import os
import sys

# Création du socket et connxion au serveur
socket_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    socket_connexion.connect(('127.0.0.1', 8080))
    print("Connecté au serveur sur 127.0.0.1: 8080")
except ConnectionRefusedError as e:
    print("Connexion refusée.Veuillez vous assurez que le serveur est bien actif.")
    sys.exit(1)
    
# Création d'un processus enfant
pid = os.fork()  # le code utilise os.fork, qui ne fonctionne que sur UNIX/Linux. Pour que cela marche sur Windows, il faut utiliser multiprocesssing au lieu de os.fork

if pid:
    # je suis le parent, processus parent:  envoi des messages au serveur; il permet à l'utilisateur de saisir des messages via input qui sont envoyés au serveur
    try:
        while True:
            ligne = input(">")
            if not ligne: # Si l'utilisateur appuie sur Entrée sans mettre de texte
                print("Fin de la connexion.")
                break
            socket_connexion.sendall(ligne.encode('utf8'))  
    except KeyboardInterrupt: # try-except pour gérer les erreurs réseau et les interruptions utilisateur
        print("\nInterruption par l'utilisateur.")
    finally:
        socket_connexion.close() # la connexion se termine proprement quand l'utilisateur ne met aucun texte ou interrompt le programme
else:
    # je suis l'enfant, processus enfant: réception des messages du serveur; il permet d'afficher les réponses du serveur en temps réel
    try:
        while True:
        ligne = socket_connexion.recv(1024)
        if not ligne: # Fin de la connexion
            print("Connexion fermée par le serveur.")
            break
        print("Mesage reçu:", ligne.decode('utf-8'))  # les messages reçus via recv sont décodés en UTF-8 avant d'être affichés
    except KeyboardInterrupt:  # try-except pour gérer les erreurs réseau et les interruptions utilisateur
        print("\nInterruption par l'utilisateur.")
    finally: # le socket est fermé correctement dans tous les cas grâce à l'utilisation de finally
        socket_connexion.close() # la connexion se termine proprement quand l'utilisateur ne met aucun texte ou interrompt le programme
