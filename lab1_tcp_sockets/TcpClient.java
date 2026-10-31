package Test;

import java.io.*;
import java.net.*;
import java.swing.JOptionPane;

public class client {
  public static void main(String[] args) {
    String ServerName = "127.0.0.1";
    int port = 9500;
    Socket ConnectionAUnServeur;

    DataInputStream FluxEntree;
    DataOutputStream FluxSortie;
    String MessageTransmettre;
    try {
      Systeme.out.println("Lancement de l'application Client" + InetAddress.getLocalHost());
      ConnectionAUnServeur = new Socket(InetAddress.getByName(ServerName), port);
      FluxSortie = new DataOutputStream(ConnectionAUnServeur.getOutputStream());
      FluxEntree = new DataInputStream(ConnectionAUnServeur.getInputStream());
      do {
        MessageTransmettre = JOptionPane.showInputDialog("Entrez un message : ");
        byte[] b = new byte[MessageTransmettre.length()];
        int i = 0;
        for (char c : MessageTransmettre.toCharArray()) {
          b[i++] = (byte) c;
        }
        FluxSortie.write(b);
      } while (!MessageTransmettre.equals("FIN"));

      System.out.println("Fermeture de la connexion");
      ConnectionAUnServeur.close();
    } catch (Exception e) {
      System.out.println("Erreur : " + e);
    }
  }
}
