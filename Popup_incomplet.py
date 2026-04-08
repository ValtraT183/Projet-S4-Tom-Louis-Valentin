from tkinter import *


def afficherPopUpIncomplet(parent):

    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Veuillez saisir toutes les données").pack()

    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()