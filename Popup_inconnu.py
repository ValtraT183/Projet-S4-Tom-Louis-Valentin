from tkinter import *


def afficherPopUpInconnu(parent):

    fen = Toplevel(parent)

    Label(fen, text="L'identifiant ou le mot de passe est incorrect").pack()


    def retour():

        fen.destroy()

    Button(fen, text="Retour", command=retour).pack()
