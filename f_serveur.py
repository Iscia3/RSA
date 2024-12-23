#!/usr/bin/env python3

import socket
import os

socket_attente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_attente.bind(('', 8080))
socket_attente.listen(socket.SOMAXCONN)

(socket_connectee, TSAP_client) = socket_attente.accept()
print(TSAP_client)
pid = os.fork()

if pid:
    # je suis le parent
    while 1:
        ligne = socket_connectee.recv(1024)
        dico_message_recu = loads(ligne)
        if dico_message_recu["type"] == "message":
            message_crypte = dico_message_recu["data"]
        if not ligne:
            break
        print(ligne)
else:
    # je suis l'enfant
    while 1:
        ligne = input(">")
        if not ligne:
            break
        socket_connectee.sendall(ligne.encode('utf8'))
socket_connectee.close()
