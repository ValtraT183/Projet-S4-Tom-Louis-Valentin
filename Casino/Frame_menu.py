from tkinter import *
from PIL import Image, ImageTk 

def creerFrameMenu(parent, retourner, nom_uti, solde_uti, quitter, creerMachineASous, creerJeuDeDes, creerBlackjack, creerRoulette):

    # Création de la frame
    frame_menu = Frame(parent, width=1500, height=750)

    # Création du canva
    canva = Canvas(frame_menu, width=1500, height=750)
    canva.pack()

    # Fond de la fenêtre
    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)


    # Titre
    canva.titre = PhotoImage(file="Image/titre.png").subsample(2)
    canva.create_image(750,100,image = canva.titre)


    # Création des boutons
    blackjack = Button(canva,text = "BlackJack",width=50,height=2, command=creerBlackjack)
    blackjack.place(x=580,y=250)

    machine = Button(canva,text="Machine à sous",width=50,height=2, command=creerMachineASous)
    machine.place(x=580,y=350)

    roulette = Button(canva,text="Roulette",width=50,height=2, command=creerRoulette)
    roulette.place(x=580,y=450)


    des = Button(canva,text="Jeu de dés",width=50,height=2, command=creerJeuDeDes)
    des.place(x=580,y=550)

    retour = Button(canva, text="Se déconnecter", width=30, height=2, command=retourner)
    retour.place(x=1250, y=600)

    quitter = Button(canva,text="Quitter",width=30,height=2, command=quitter)
    quitter.place(x=1250,y=700)



    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")

    canva.create_text(1350,100,text=f"Solde : {solde_uti} VTL",font=("Arial",15),fill="white")

    return{
        "frame": frame_menu,
        "nom": nom_uti,
        "mdp": solde_uti
    }




