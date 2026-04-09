from tkinter import *


def afficherPopUp18ans(parent):
    """
    Création d'une nouvelle fenêtre avec le texte associé au problème
    """
    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Vous n'avez pas l'âge requis (18 ans minimum)").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
