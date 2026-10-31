import socket
import _thread

def traiter_connexion(connexion, addrclient):
    print("Connexion de la machine = ", addrclient)
    MessageRec=""
    try:
        while (MessageRec.strip().lower() != "fin"):
            MessageRec = connexion.recv(1024)
            MessageRec = MessageRec.decode()
            print("client: ", addrclient, " message: ", MessageRec)
    exept:
        print("Deconnexion")
    print("Deconnexion de :", addrclient)
    try:
        addrclient.close()
    except:
        pass

SocketServeur = socket.socket()
host = socket.gethostname()
port = 9500
SocketServeur.bind(("127.0.0.1", port))

SocketServeur.listen(1)

print("lancement serveur")
while True:
    ConnexionAUnClient, addrclient = SocketServeur.accept()
    _thread.start_new_thread(traiter_connexion, (ConnexionAUnClient, addrclient))
