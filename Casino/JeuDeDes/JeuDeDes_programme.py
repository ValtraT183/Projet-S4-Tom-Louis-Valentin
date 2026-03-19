# Programme Jeu de Dé Projet Casino S4

import random
from tkinter import *
from PIL import Image, ImageTk 

# CONSTANTES
VTL_DEPART = 100
MISE_MIN = 5
NB_DES = 3


# FONCTIONS DU JEU
def lancer_des(nombre_de_des):
    return[random.randint(1,6) for _ in range(nombre_de_des)]

def calculer_somme(liste_des):
    return sum(liste_des)

def determiner_resultat(somme_joueur, somme_croupier):
    if somme_joueur > somme_croupier:
        return "Victoire"
    elif somme_joueur < somme_croupier:
        return "Defaite"
    else :
        return "Egalité"
    
def calculer_gain(mise, resultat_du_tour):
    if resultat_du_tour == "Victoire":
        return mise
    elif resultat_du_tour == "Defaite":
        return -mise
    else :
        return 0


# INTERFACES TKINTER

# Création de la fenêtre
fenetre = Tk()
fenetre.title("Casino")
fenetre.iconbitmap("casinologo.ico")
fenetre.geometry("1500x750")

# Création du canva
canva = Canvas(fenetre, width=1500, height=750)
canva.place(x = 0,y = 0)


# Fond de la fenêtre
image = Image.open("background.png")
image = image.resize((1500, 750))
photo_background = ImageTk.PhotoImage(image)
canva.create_image(0, 0, anchor=NW, image=photo_background)

# Image LOGO
logo = PhotoImage(file="casinologoSF.png").subsample(4)
canva.create_image(20,30,image=logo)




fenetre.mainloop()

"""
# TOUR DU JEU
def _mise_valide(self):
    try:
        mise = int(self.var_mise.get())
        return MISE_MIN <= mise <= self.solde
    except ValueError:
        return False

def _tour(self):
    if not self._mise_valide():
        try:
            mise = int(self.var_mise_get())
            if mise < MISE_MIN: 
                self
"""
