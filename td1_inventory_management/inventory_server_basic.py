from socket import socket
server = socket()
server.bind(('0.0.0.0',747))

server.listen(5)
list_arcticle = {"USB" : 7 ,"imprimont canon" : 3, "GPU voodo 3" : 0}

while True:
    con,addr = server.accept()
    data = con.recv(1024).decode().strip()
    operation,nomArticle,quantite= data.split(" ")#Ligne 8
    quantite = int(quantite)
    if operation not in ["Ravitailler","Destocker"]:
        con.send("#Operation non valide".encode())
        con.close()
        continue
    if nomArticle not in list_arcticle:
        con.send("#Article introuvable".encode())
        con.close()
        continue
    if operation == "Destocker" and list_arcticle[nomArticle] < quantite:
        con.send("#Quantite insufisante".encode())
        con.close()
        continue
    if operation == "Ravitailler":
        list_arcticle[nomArticle] += quantite
    else:
        list_arcticle[nomArticle] -= quantite
    con.send(f"OK {list_arcticle[nomArticle]}".encode())
    con.close()

