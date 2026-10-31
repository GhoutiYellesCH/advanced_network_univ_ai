import socket
SocketUDP= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # ceration socket UDP
SocketUDP.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) # rendre le socket UDP broadcast
Numero_Port=5000
AdresseDiffusion='192.168.139.255'
MessageADiffuser=b'Votre message a diffuser dans le reseau'
SocketUDP.sendto(MessageADiffuser, (AdresseDiffusion, Numero_Port)) 
