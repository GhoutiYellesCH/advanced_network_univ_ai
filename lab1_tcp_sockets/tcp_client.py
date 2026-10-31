import socket 

connexinAuServeur = socket.socket()
host = "127.0.0.1"
port = 9500
print("Console client")
ConnexionAuServeur.connect((host, port))
MessageAEnvoyer = ""

while MessageAEnvoyer.strip().lower() != "fin":
    MessageAEnvoyer = input("Entrez un message a envoyer au serveur: ")
    ConnexionAuServeur.send(MessageAEnvoyer.encode())

ConnexionAuServeur.close()
print("Fin de la connexion")
