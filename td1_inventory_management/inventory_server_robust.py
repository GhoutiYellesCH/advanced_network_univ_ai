from socket import socket

serveur = socket()
serveur.bind(("0.0.0.0", 747))
serveur.listen(5)
liste_articles = {"USB": 7, "Imprimante Canon": 3, "GPU Voodoo": 0}

while True:
    con, addr = serveur.accept()
    try:
        data = con.recv(1024).decode().strip()
        operation, nom_article, quantite_str = data.split(" ")
        quantite = int(quantite_str)
    except ValueError as e:
        if 'not enough' in str(e) or 'too many' in str(e):
            con.send("#Commande invalide".encode())
        else:
            con.send("#Quantite invalide".encode())
        con.close()
        continue
    except Exception as e:
        con.send("#Erreur".encode())
        con.close()
        continue

    if operation not in ["Ravitailler", "Destocker"]:
        con.send("#Operation non valide".encode())
        con.close()
        continue

    if nom_article not in liste_articles:
        con.send("#Article introuvable".encode())
        con.close()
        continue

    if operation == "Destocker" and liste_articles[nom_article] < quantite:
        con.send("#Quantite insufisante".encode())
        con.close()
        continue

    if operation == "Ravitailler":
        liste_articles[nom_article] += quantite
    else:
        liste_articles[nom_article] -= quantite

    con.send(f"OK {liste_articles[nom_article]}".encode())
    con.close()
