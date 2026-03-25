from tkinter import *


def afficherPopUp18ans(parent):

    fen = Toplevel(parent)

    Label(fen, text="Vous n'avez pas l'âge requis (18 ans minimum)").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
