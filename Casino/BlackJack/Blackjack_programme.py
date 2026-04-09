from PIL import Image, ImageTk 


def recup_image(carte):
        """
        Cette fonction récupère les images des cartes dans le dossier image
        """

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


def calcul_score(liste_carte):
        """
        Cette fonction calcule le score d'une liste de carte
        """
        somme = 0
        nb_as = 0
        for carte in liste_carte:
                somme = somme + cartes_dict[carte]      #calcul de la somme
                
                if carte[-2:] == "as":
                        nb_as += 1

        if nb_as == 0:
                return somme
        
        else:
                while nb_as > 1:
                        somme = somme - 10
                        nb_as = nb_as - 1

                if somme > 21:
                        somme = somme - 10
                elif somme <= 21:
                        return (somme, somme-10)
        return somme





#Fonction pour calculer le gain du joueur en fonction de la mise
def recup_gain(mise, win):
        """
        win = 0 --> le joueur a perdu
        win = 1 --> le joueur a gagné
        win = 2 --> égalité
        win = 3 --> Blackjack
        """
        if win == 0:
                return 0
        elif win == 2:
                return mise
        elif win == 1:
                return mise*2
        elif win == 3:
                return mise*3
