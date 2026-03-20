from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*
from Casino.Blackjack.Blackjack_programme import*




def creerFrameBlackjack(parent, fin_jeu, nom, solde, quitter):

    def jouer():
        pass



 
    
    #Création de la frame

    frame_blackjack = Frame(parent, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_blackjack, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

    
    # Titre
    canva.create_text(200,50,text="Blackjack",fill='white',font=("Arial",40))

    canva.create_line(400,0,400,750,fill="black",width=2)


   
    # Création des tables


    # table du haut

    canva.create_line(550,100,950,100,fill="white",width="2")
    canva.create_line(550,250,950,250,fill="white",width="2")
    canva.create_line(550,100,550,250,fill="white",width="2")
    canva.create_line(950,100,950,250,fill="white",width="2")


    # table du bas 

    canva.create_line(550,650,950,650,fill="white",width="2")
    canva.create_line(550,500,950,500,fill="white",width="2")
    canva.create_line(550,500,550,650,fill="white",width="2")
    canva.create_line(950,500,950,650,fill="white",width="2")

   



    # Affichage des totaux
    total_banque = canva.create_text(750,270,text=f"Total banque : {0}",fill='white',font=("Arial",20))
    total_joueur = canva.create_text(750,480,text=f"Total : {0}",fill='white',font=("Arial",20))


    # Création du bouton quitter

    quitter = Button(canva,text="Quitter",width=30,height=2, command=quitter)
    quitter.place(x=1250,y=700)
        


    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)





    # Création bouton lancer les dés

    lancer = Button(canva,text="cartes",width=20,command=jouer)
    lancer.place(x=100,y=400)
        



    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly")
    mise.place(x=300,y=400)    
    


    # Affichage gain total 

    gain = canva.create_text(1300,350,text=f"Gain : {0}",fill='white',font=("Arial",20))





    return {
        "frame": frame_blackjack,
        "nom_uti": nom,
        "solde_uti": solde,
    }