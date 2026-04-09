from tkinter import *


def afficherPopUpPasDeVTL(parent):
    """
    Création d'une nouvelle fenêtre avec le texte associé au problème
    """
    fen = Toplevel(parent)
    fen.iconbitmap("Image/casinologo.ico")

    canva = Canvas(fen, height=300, width=500)
    canva.pack()

    canva.create_text(150,50, text="Vous n'avez plus de VTL, votre compte est supprimé")

    def decompte(i):
        """
        Fonction pour afficher le décompte de 5 secondes avant le retour au menu
        """
        i=i-1
        canva.delete("temps")
        if i>0:
            if i>1:
                canva.create_text(250,150,text=f"Vous serez redirigé vers la page de connexion dans {i} secondes", tags="temps")
            else:
                canva.create_text(250,150,text=f"Vous serez redirigé vers la page de connexion dans {i} seconde", tags="temps")
            canva.after(1000, lambda : decompte(i))

        else:
            fen.destroy()

    decompte(5)