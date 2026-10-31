from socket import socket

while True:
    print("in format of operation , nom_article , quantite")
    cmd = input("Commande (Ravitailler/Destocker Nom Quantité): ")
    if cmd.lower() == 'exit':
        break
    client = socket()
    client.connect(("localhost", 747))
    client.send(cmd.encode())
    reponse = client.recv(1024).decode()
    print("Réponse:", reponse)
    client.close()
