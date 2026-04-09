from tkinter import *


def afficherPopUppolitique(parent):
    """
    Création d'une nouvelle fenêtre avec le texte associé au problème
    """
    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Vous n'avez pas accepté les règles de confidentialité").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
