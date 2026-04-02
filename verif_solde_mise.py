from Popup_solde_insuffisant import affichierPopUpSoldeInsuffisant
from Popup_pasdeVTL import afficherPopUpPasDeVTL


def supprimer_compte(nom):
        lignes=[]
        nouvelles_lignes=[]

        with open("Compte.txt","r",encoding="utf-8") as compte:
            lignes=compte.readlines()

            for el in lignes:
                joueur = el.strip()
                joueur = joueur.split("/")
                if joueur[0] != nom:
                    nouvelles_lignes.apppend(el)

        with open("Compte.txt", "w", encoding="utf-8") as fichier:
            fichier.writelines(nouvelles_lignes) 


def verif_mise(fenetre,solde,mise):
    if solde-mise >= 0:
        return True
    else:
        affichierPopUpSoldeInsuffisant(fenetre)
        return False


def verif_solde(fenetre,solde,nom):
    if solde >= 5:
        return True
    else:
        afficherPopUpPasDeVTL(fenetre)
        supprimer_compte(nom)
