from PIL import Image, ImageTk 


def recup_image(carte):

        img = Image.open(f"Image/{carte}.png")
        img = img.resize((100,150))
        return ImageTk.PhotoImage(img)
        

cartes_dict = {
        "carreau-2": 2, "carreau-3": 3, "carreau-4": 4, "carreau-5": 5, "carreau-6": 6, "carreau-7": 7,
        "carreau-8": 8, "carreau-9": 9, "carreau-10": 10, "carreau-valet": 10, "carreau-dame": 10, "carreau-roi": 10, "carreau-as": 11,

        "coeur-2": 2, "coeur-3": 3, "coeur-4": 4, "coeur-5": 5, "coeur-6": 6, "coeur-7": 7,
        "coeur-8": 8, "coeur-9": 9, "coeur-10": 10, "coeur-valet": 10, "coeur-dame": 10, "coeur-roi": 10, "coeur-as": 11,

        "trefle-2": 2, "trefle-3": 3, "trefle-4": 4, "trefle-5": 5, "trefle-6": 6, "trefle-7": 7,
        "trefle-8": 8, "trefle-9": 9, "trefle-10": 10, "trefle-valet": 10, "trefle-dame": 10, "trefle-roi": 10, "trefle-as": 11,

        "pique-2": 2, "pique-3": 3, "pique-4": 4, "pique-5": 5, "pique-6": 6, "pique-7": 7,
        "pique-8": 8, "pique-9": 9, "pique-10": 10, "pique-valet": 10, "pique-dame": 10, "pique-roi": 10, "pique-as": 11
        }       

def score_joueur(carte_joueur):
        somme = 0
        for carte in carte_joueur:
                somme = somme + cartes_dict[carte]      #calcul de la somme

        for carte in carte_joueur:      # as = 11 ou 1
                if carte[-2:] == "as":
                        if somme > 21:
                                somme = somme-10
                        elif somme ==21:
                                return somme
                        else:
                                return (somme, somme-10)
        return somme


def score_croupier(carte_croupier):
        somme = 0
        for carte in carte_croupier:
                somme = somme + cartes_dict[carte]      #calcul de la somme

        for carte in carte_croupier:      # as = 11 ou 1
                if carte[-2:] == "as":
                        if somme > 21:
                                somme = somme-10
                        elif somme ==21:
                                return somme
                        else:
                                return (somme, somme-10)
        return somme
