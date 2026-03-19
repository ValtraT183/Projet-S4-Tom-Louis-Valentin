from tkinter import *


def afficherPopUppolitique(parent):

    fen = Toplevel(parent)

    Label(fen, text="Vous n'avez pas accepté les règles de confidentialité").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
