from tkinter import *
from winsound import *

from Frame_connexion import creerFrameConnexion
from Casino.Frame_menu import creerFrameMenu
from Frame_creerCompte import creerFrameCreerCompte

#importation PopUp
from Popup_incomplet import afficherPopUpIncomplet
from Popup_inconnu import afficherPopUpInconnu
from Popup_18ans import afficherPopUp18ans
from Popup_politique import afficherPopUppolitique
from Popup_nompris import afficherPopUpnompris

#importation Jeux

from Casino.MachineASous.Frame_machineASous import creerFrameMachineASous
from Casino.JeuDeDes.Frame_jeuDeDes import creerFrameJeuDeDes
from Casino.Blackjack.Frame_blackjack import creerFrameBlackjack
from Casino.Roulette.Frame_roulette import creerFrameRoulette




#variables globales
nom_uti = ""
mdp_uti = ""
solde_uti = 0
frame_menu = None
frame_machine_a_sous = None
frame_jeu_de_des = None
frame_blackjack = None
frame_roulette = None


# Création d'un objet "fenêtre"
fenetre = Tk()
# Titre de la fenêtre
fenetre.title("Casino")
# Taille de la fenêtre
fenetre.geometry("1500x750")
fenetre.iconbitmap("Image/casinologo.ico")

fenetre.resizable(width=False, height=False)
fenetre.minsize(width=1500, height=750)


#Récupérer le solde après chaque actualisation du txt
def recup_solde(nom):
    with open("Compte.txt", "r", encoding="utf-8") as compte:
        lignes=compte.readlines()
        for el in lignes:
            joueur = el.strip()
            joueur = joueur.split("/")
            if joueur[0] == nom:
                return int(joueur[2])


def fermer() :
    PlaySound(None,0)
    fenetre.destroy()

# Frames Jeux


# Quitter le jeu / retour au menu
def jeuToMenu(frame_jeu):
    global frame_menu
    global nom_uti

    nouveau_solde = recup_solde(nom_uti)

    frame_menu = creerFrameMenu(fenetre, menuToConnexion, nom_uti, nouveau_solde, fermer, creerMachineASous, creerJeuDeDes, creerBlackjack, creerRoulette) #recréer menu avec nouveau solde
    frame_jeu["frame"].pack_forget()
    frame_menu["frame"].pack(fill="both", expand=True)

def fin_jeu_JeuDeDes():
    global frame_jeu_de_des
    jeuToMenu(frame_jeu_de_des)

def fin_jeu_MachineAsous():
    global frame_machine_a_sous
    jeuToMenu(frame_machine_a_sous)

def fin_jeu_Blackjack():
    global frame_blackjack
    jeuToMenu(frame_blackjack)

def fin_jeu_Roulette():
    global frame_roulette
    jeuToMenu(frame_roulette)

# Le joueur n'a plus de VTL, retour au menu connexion
def jeuToConnexion(frame_jeu): # Fonction pour revenir au menu connexion lorsque le joueur n'a plus assez d'argent pour jouer.
    global frame_connexion

    frame_jeu["frame"].pack_forget()
    frame_connexion["frame"].pack(fill="both", expand=True) #échange des frames => retour jeu à menu connexion

def blackjackToConnexion():
    global frame_blackjack
    jeuToConnexion(frame_blackjack)

def jeuDeDesToConnexion():
    global frame_jeu_de_des
    jeuToConnexion(frame_jeu_de_des)

def machineASousToConnexion():
    global frame_machine_a_sous
    jeuToConnexion(frame_machine_a_sous)

def rouletteToConnexion():
    global frame_roulette
    jeuToConnexion(frame_roulette)



# Afficher les jeux


def creerMachineASous():
    global frame_menu
    global frame_machine_a_sous

    nouveau_solde = recup_solde(nom_uti)

    frame_machine_a_sous = creerFrameMachineASous(fenetre, fin_jeu_MachineAsous, nom_uti, nouveau_solde, fermer,machineASousToConnexion)

    frame_menu["frame"].pack_forget()
    frame_machine_a_sous["frame"].pack(fill="both", expand=True) #échange des frames => retour menu machine à sous à menu casino


def creerJeuDeDes():
    global frame_menu
    global frame_jeu_de_des
    nouveau_solde = recup_solde(nom_uti)

    frame_jeu_de_des = creerFrameJeuDeDes(fenetre, fin_jeu_JeuDeDes, nom_uti, nouveau_solde,fermer,jeuDeDesToConnexion)

    frame_menu["frame"].pack_forget()
    frame_jeu_de_des["frame"].pack(fill="both", expand=True) #échange des frames => retour menu jeu de dés à menu casino


def creerBlackjack():
    global frame_menu
    global frame_blackjack
    nouveau_solde = recup_solde(nom_uti)

    frame_blackjack = creerFrameBlackjack(fenetre, fin_jeu_Blackjack, nom_uti, nouveau_solde,fermer,blackjackToConnexion)

    frame_menu["frame"].pack_forget()
    frame_blackjack["frame"].pack(fill="both", expand=True) #échange des frames => retour menu jeu de dés à menu casino


def creerRoulette():
    global frame_menu
    global frame_roulette
    nouveau_solde = recup_solde(nom_uti)

    frame_roulette = creerFrameRoulette(fenetre, fin_jeu_Roulette, nom_uti, nouveau_solde, fermer,rouletteToConnexion)

    frame_menu["frame"].pack_forget()
    frame_roulette["frame"].pack(fill="both", expand=True) #échange des frames => retour menu machine à sous à menu casino

 

# Fonctions valider connexion

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
                frame_menu = creerFrameMenu(fenetre, menuToConnexion, nom_uti, solde_uti, fermer, creerMachineASous, creerJeuDeDes, creerBlackjack, creerRoulette) #on passe au menu
                frame_menu["frame"].pack(fill="both", expand=True) #on affiche le menu
                return None

    return afficherPopUpInconnu(fenetre) #erreur identifiant ou mdp inconnu


# Fonction valider création compte
def actualiserTxt(nom,mdp):
    with open("Compte.txt","a",encoding="utf-8") as compte :
        compte.write(f"{nom}/{mdp}/{1000}\n")

def valider_nouveau_compte():
    if frame_creer_compte["id"].get() == "" or frame_creer_compte["mdp"].get() == "" or frame_creer_compte["age"].get() == "":
        return afficherPopUpIncomplet(fenetre)

    nom = frame_creer_compte["id"].get()   #on récupère son nom 
    mdp = frame_creer_compte["mdp"].get()  #on récupère son mdp
    age = int(frame_creer_compte["age"].get())  #on récupère son age
    politique = frame_creer_compte["politique"].get()

    frame_creer_compte["id"].delete(0,'end')
    frame_creer_compte["mdp"].delete(0,'end')
    frame_creer_compte["age"].set("")       #Vider les Entry
    frame_creer_compte["politique"].set(0)

    if age < 18:           # Vérification age
        return afficherPopUp18ans(fenetre)
    
    if not politique:   # Vérification politique
        return afficherPopUppolitique(fenetre)
    

    liste=[]
    with open("Compte.txt", "r",encoding="utf-8") as compte:
            ligne=compte.readlines()
    for i in ligne:
        liste.append(i.split("/"))

    for el in liste:
        el[2] = el[2][:-1]

    for el in liste:        #Vérification que le nom n'est pas déjà utilisé
        if nom == el[0]:
            return afficherPopUpnompris(fenetre)
    
    return actualiserTxt(nom,mdp), CreerCompteToConnexion()
    



# Fonction afficher menu creer compte
frame_creer_compte = None
def creerCreerCompte():
    global frame_connexion
    global frame_creer_compte

    frame_creer_compte = creerFrameCreerCompte(fenetre, CreerCompteToConnexion, valider_nouveau_compte,fermer)

    frame_connexion["frame"].pack_forget()
    frame_creer_compte["frame"].pack(fill="both", expand=True) #échange des frames => retour menu jeu de dés à menu casino



# Fonction retour menu creercompte à menu connexion
def CreerCompteToConnexion():
    frame_creer_compte["frame"].pack_forget()
    frame_connexion["frame"].pack(fill="both", expand=True) #échange des frames => retour menu casino à menu connexion



# Fonction retour menu casino à menu connexion
def menuToConnexion():
    frame_menu["frame"].pack_forget()
    frame_connexion["frame"].pack(fill="both", expand=True) #échange des frames => retour menu casino à menu connexion




# Affichage menu connexion
frame_connexion = creerFrameConnexion(fenetre, valider,fermer, creerCreerCompte)
frame_connexion["frame"].pack(fill="both", expand=True)



# Pour la musique 
fenetre.protocol("WM_DELETE_WINDOW", fermer)  # au lieu de fermer la fenêtre quand on appuye sur la croix, ça exécute la fonction)
PlaySound("Son/musique.wav",SND_ASYNC | SND_LOOP)


 

# Démarrage de la boucle Tkinter (à placer à la fin !!!)
fenetre.mainloop()