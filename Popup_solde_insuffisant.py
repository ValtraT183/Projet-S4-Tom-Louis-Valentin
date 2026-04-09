from tkinter import *


def afficherPopUpSoldeInsuffisant(parent):
    """
    Création d'une nouvelle fenêtre avec le texte associé au problème
    """
    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Votre solde ne vous permet pas miser de autant de VTL.").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
