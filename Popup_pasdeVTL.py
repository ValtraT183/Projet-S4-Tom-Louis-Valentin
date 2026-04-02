from tkinter import *


def afficherPopUpPasDeVTL(parent):

    fen = Toplevel(parent)

    Label(fen, text="Vous n'avez plus de VTL, votre compte est supprimé").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
