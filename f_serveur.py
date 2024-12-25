#!/usr/bin/env python3

import socket
import os
import json

# Création du socket serveur
socket_attente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_attente.bind(('', 8080))
socket_attente.listen(socket.SOMAXCONN)

print("Serveur en attente de connexion...")
(socket_connectee, TSAP_client) = socket_attente.accept()
print(f"Connexion établie avec: {TSAP_client}")

# Création d'un processus enfant
pid = os.fork()

if pid:
    # je suis le parent, processus parent: Réception des messages
    try:
        while True:
        ligne = socket_connectee.recv(1024)
        if not ligne:
            print("Connexion fermée par le client.")
            break
        try:
            # Dissociation du message JSON
            dico_message_recu = json.loads(ligne.decode('utf-8')) # les messages JSON reçus sont correctement dissociés avec json.loads
            if dico_message_recu["type"] == "message":
            message_crypte = dico_message_recu["data"]
            print("Message chiffré reçu:", message_crypte)
        else:
            print("Type de message inconnu:", dico_message_recu)
    except json.JSONDecodeError as e: # gestion des erreurs réseau et des interruptions utilisateur pour éviter des plantages
        print(f"Erreur de décodage JSON: {e}")
except KeyboardInterrupt:
    print("\nInterruption par l'utilisateur.")
finally: # socket fermé proprement dans un bloc finally pour garantir une libération des ressources
    socket_connectee.close()
    socket_attente.close()
else:
    # je suis l'enfant, processus enfant: envoi des messages
    try:
        while True:
            ligne = input(">")
            if not ligne:
                print("Fin de la connexion.")
                break
            # Envoi d'un message sous forme de JSON
            dico_message = {"type": "message", "data": ligne} # le message envoyé est un dictionnaire JSON avec un champ "type" et un champ "data", ce qui rend le format extensible
            socket_connectee.sendall(json.dumps(dico_message).encode('utf8')) # les messages envoyés sont associés avec json.dumps
    except KeyboardInterrupt: # gestion des erreurs réseau et des interruptions utilisateur pour éviter des plantages
        print("\nInterruption par l'utilisateur.")
    finally:  # socket fermé proprement dans un bloc finally pour garantir une libération des ressources
        socket_connectee.close()
