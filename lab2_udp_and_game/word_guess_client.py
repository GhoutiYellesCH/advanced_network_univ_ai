import socket

try:
    client = socket.socket()
    
    client.connect(("localhost", 900))

    data = client.recv(1024).decode("ascii")
    
    if not data:
        print("Erreur: Aucun mot reçu du serveur.")
        client.close()
        exit()

    mot_melange = data.split("#")[0]
    print(f"Mot mélangé reçu : {mot_melange}")

    while True:
        guess = input("Votre réponse : ").strip()
        
        client.send((guess + "#TRY\r\n").encode("ascii"))
        
        response = client.recv(1024).decode("ascii")
        
        if "#YOUWON" in response:
            print("Bravo !", response)
            break
        elif "#WRONG" in response:
            print("Mauvaise réponse, essayez encore !")
        else:
            print("Erreur: Réponse inattendue du serveur.")

    client.send(b"#FINISH\r\n")
    client.close()

except ConnectionRefusedError:
    print("Erreur: Impossible de se connecter au serveur. Assurez-vous qu'il est en cours d'exécution.")
except Exception as e:
    print(f"Erreur inattendue : {e}")
finally:
    client.close()

