#!/usr/bin/env python3

import socket
import os

socket_connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_connexion.connect(('127.0.0.1', 8080))

pid = os.fork()

if pid:
    # je suis le parent
    while 1:
        ligne = input(">")
        if not ligne:
            break
        socket_connexion.sendall(ligne.encode('utf8'))
else:
    # je suis l'enfant
    while 1:
        ligne = socket_connexion.recv(1024)
        if not ligne:
            break
        print(ligne)
socket_connexion.close()
