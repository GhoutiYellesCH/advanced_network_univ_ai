import socket

SocketServeur = socket.socket()
port = 9500
# creation d'un socket en ecout sur l'interface 127.0.0.1, port=9500
SocketServeur.bind(("127.0.0.1", port))
SocketServeur.listen(1) # nombre de maximale de connexion qui peuvent etre misen file d'attente

print( "Lancement serveur") # instruction d'affichage
while True: # boucle infinie
    # accept bloque le programme en attendant une connexion d'un client (la reception du SYN)
    ConnexionAUnClient, addrclient = SocketServeur.accept()
    # une fois que la connexion est recue, accept renvoie l'adresse du client et un objet socket
    # permetant l'envoie et la reception sur cette connexion

    print("Connexion de la machine = ", addrclient)

    MessageRec=""

    while(MessageRec.strip().lower()!="fin"):# tanque le message recu est different de "fin"

        MessageRec=ConnexionAUnClient.recv(1024) # recv permet de recevoir une sequence d'octets

        print( MessageRec.decode())

        # .decode() transforme une objet bytes (suite d'octets) en chaine de caracteres en

    print( "Deconnexion de :",addrclient)
    #ConnexionAUnClient.close() # coloture la connexion (envoie FIN ACK au client)
