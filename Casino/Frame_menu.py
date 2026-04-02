from tkinter import *
from PIL import Image, ImageTk 
from random import*



def creerFrameMenu(parent, retourner, nom_uti, solde_uti, quitter, creerMachineASous, creerJeuDeDes, creerBlackjack, creerRoulette):
    
    
   
    def affichageNewsletter(liste):
        canva.delete("newsletter")
        info = randint(0,len(liste)-1)
        canva.create_text(65,350,text=liste[info],font=("Arial",15),fill="white",tags="newsletter",anchor=W)
        canva.after(10000,lambda :affichageNewsletter(liste))


    

    def indiceSoldeLePlusHaut():
        with open("Compte.txt","r",encoding="utf8") as compte :
            lignes = compte.readlines()
            soldes = []
            for ligne in lignes :
                liste = ligne.strip().split("/")
                soldes.append(int(liste[2])) 
            haut = soldes[0]
            indice=0
            for i in range(len(soldes)):
                if soldes[i] > haut :
                    indice = i
                    haut = soldes[i]

            return indice
                    
                

    def nomSoldeUtiStar(indice) :
        with open("Compte.txt","r",encoding="utf8") as compte :
            lignes = compte.readlines()
            info_joueur = lignes[indice].strip().split("/")
            return (info_joueur[0],info_joueur[2])
        

    

   
    
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

    quitt = Button(canva,text="Quitter",width=30,height=2,bg="red", command=quitter)
    quitt.place(x=1250,y=700)



    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")
    canva.create_text(1350,100,text=f"Solde : {solde_uti} VTL",font=("Arial",15),fill="white")


    # Affichage de la newsletter
    nom,solde= nomSoldeUtiStar(indiceSoldeLePlusHaut())
    newsletter = [f"Utilisateur stars : {nom}, {solde} VTL"]
    
    canva.create_text(225,150,text="Newsletter",fill='gold',font="Rye 37")
    
    canva.create_line(50,100,400,100,width=4,fill = "gold")
    canva.create_line(50,675,400,675,width=4,fill = "gold")
    
    canva.create_line(50,100,50,675,width=4,fill = "gold")
    canva.create_line(400,100,400,675,width=4,fill = "gold")

    affichageNewsletter(newsletter)





    return{
        "frame": frame_menu,
        "nom": nom_uti,
        "solde_uti": solde_uti
    }




