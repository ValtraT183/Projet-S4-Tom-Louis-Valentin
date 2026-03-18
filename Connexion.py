from tkinter import *
from PIL import Image, ImageTk
from Frame_connexion import creerFrameConnexion
from Casino.Menu import creerFrameMenu
from Popup_incomplet import afficherPopUpIncomplet
from Popup_inconnu import afficherPopUpInconnu




#variables globales
nom_uti = ""
mdp_uti = ""
solde_uti = 0
frame_menu = None


# Création d'un objet "fenêtre"
fenetre = Tk()
# Titre de la fenêtre
fenetre.title("Casino - Connexion")
# Taille de la fenêtre
fenetre.geometry("1500x750")



# Fonctions

def valider():
    global nom_uti
    global mdp_uti
    global solde_uti
    global frame_menu

    # Vérification que les entrées sont remplis
    if frame_connexion["id"].get() == "" or frame_connexion["mdp"].get() == "":
        return afficherPopUpIncomplet(fenetre)
    
    nom_uti = frame_connexion["id"].get()   #on récupère son nom dans la variable global
    mdp_uti = frame_connexion["mdp"].get()  #on récupère son mdp dans la variable global

    # Vider les Entry
    frame_connexion["id"].delete(0,'end')
    frame_connexion["mdp"].delete(0,'end')


    liste=[]
    with open("Compte.txt", "r",encoding="utf-8") as compte:
            ligne=compte.readlines()
    for i in ligne:
        liste.append(i.split("/"))

    for el in liste:
        el[2] = el[2][:-1]


    for el in liste:
        if nom_uti == el[0]:
            if mdp_uti == el[1]:
                solde_uti = el[2] #on récupère son solde dans la variable global

                frame_connexion["frame"].pack_forget()
                frame_menu = creerFrameMenu(fenetre, retourner, nom_uti, solde_uti, fenetre.destroy) #on passe au menu
                frame_menu["frame"].pack(fill="both", expand=True) #on affiche le menu
                return None

    return afficherPopUpInconnu(fenetre) #erreur identifiant ou mdp inconnu


# Fonction retour
def retourner():

    frame_menu["frame"].pack_forget()
    frame_connexion["frame"].pack(fill="both", expand=True) #échange des frames => retour menu casino à menu connexion



#affichage menu connexion
frame_connexion = creerFrameConnexion(fenetre, valider, fenetre.destroy)
frame_connexion["frame"].pack(fill="both", expand=True)

# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()

