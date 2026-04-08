from tkinter import *


def afficherPopUpnompris(parent):

    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    Label(fen, text="Cet identifiant est déjà utilisé, veuillez en choisir un autre.").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
