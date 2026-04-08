from tkinter import *


def afficherPopUppolitique(parent):

    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Vous n'avez pas accepté les règles de confidentialité").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
