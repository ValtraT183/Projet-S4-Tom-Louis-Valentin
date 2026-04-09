from Popup_solde_insuffisant import afficherPopUpSoldeInsuffisant
from Popup_pasdeVTL import afficherPopUpPasDeVTL


def supprimer_compte(nom):
        """
        Cette fonction supprime le compte du fichier compte.txt
        """

        lignes=[]
        nouvelles_lignes=[]

        with open("Compte.txt","r",encoding="utf-8") as compte:
            lignes=compte.readlines()

            for el in lignes:
                joueur = el.strip()
                joueur = joueur.split("/")
                if joueur[0] != nom:
                    nouvelles_lignes.append(el)

        with open("Compte.txt", "w", encoding="utf-8") as fichier:
            fichier.writelines(nouvelles_lignes) 


def verif_mise(fenetre,solde,mise):
    """
    Cette fonction vérifie que la mise du joueur est en dessous de son solde, sinon affichage d'une PopUp
    """
    if solde-mise >= 0:
        return True
    else:
        afficherPopUpSoldeInsuffisant(fenetre)
        return False


def verif_solde(fenetre,solde,nom):
    """
    Cette fonction vérifie que le joueur a encore assez de VTL pour jouer
    """
    if solde >= 5:
        return True
    else:
        afficherPopUpPasDeVTL(fenetre)
        supprimer_compte(nom)

