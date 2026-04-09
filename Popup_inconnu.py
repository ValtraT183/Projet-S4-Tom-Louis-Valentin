from tkinter import *


def afficherPopUpInconnu(parent):
    """
    Création d'une nouvelle fenêtre avec le texte associé au problème
    """
    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="L'identifiant ou le mot de passe est incorrect").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
