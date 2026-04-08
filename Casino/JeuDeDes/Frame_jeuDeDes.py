from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*
from Casino.JeuDeDes.JeuDeDes_programme import recup_gain, recup_image

from Fonctions_utiles import verif_mise, verif_solde


def creerFrameJeuDeDes(fenetre, fin_jeu, nom, solde, quitter, jeuDeDesToConnexion):

    solde_joueur = int(solde)

    def jouer():
        global de1,de2,de3,de1a,de2a,de3a
        global n1,n2,n3,n1a,n2a,n3a

        if verif_mise(fenetre, solde_joueur, int(mise.get())): #Verif mise
            pass
        else:
            return None
        
        n1, n2, n3 = randint(1,6), randint(1,6), randint(1,6)
        n1a, n2a, n3a = randint(1,6), randint(1,6), randint(1,6)

        de1 = recup_image(n1)
        de2 = recup_image(n2)
        de3 = recup_image(n3)

        de1a = recup_image(n1a)
        de2a = recup_image(n2a)
        de3a = recup_image(n3a)


        # joueur du haut
        canva.create_image(625,150,image=de1a)
        canva.create_image(750,200,image=de2a)
        canva.create_image(875,150,image=de3a)

        # joueur du bas
        canva.create_image(625,550,image=de1)
        canva.create_image(750,600,image=de2)
        canva.create_image(870,550,image=de3)

        
        tot_b = n1a+n2a+n3a
        tot_u = n1+n2+n3
        canva.itemconfig(total_banque, text=f"Total banque : {tot_b}")
        canva.itemconfig(total_joueur, text=f"Total : {tot_u}")
        canva.itemconfig(gain,text=f"Gain : {recup_gain(int(mise.get()),tot_b,tot_u)}")
        
        return actualiser_solde(recup_gain(int(mise.get()),tot_b,tot_u), int(mise.get()))

    def actualiser_solde(gain, mise):
        nonlocal solde_joueur

        solde_joueur = solde_joueur - mise + gain
        canva.delete("Solde")
        canva.create_text(1350,100,text=f"Solde : {solde_joueur} VTL",font=("Arial",15),fill="white", tags="Solde")
        
        #On vérifie que le joueur à toujours assez de VTL pour jouer au casino
        if verif_solde(fenetre, solde_joueur, nom):
            pass
        else:
            lancer.config(state=DISABLED)
            retour.config(state=DISABLED)
            canva.after(5000, jeuDeDesToConnexion)

        actualiser_solde_txt(solde_joueur, nom)

    # Fonction actualiser le solde dans le txt

    def actualiser_solde_txt(nouveau_solde, nom):
        global solde_courant
        solde_courant = nouveau_solde
        lignes=[]

        with open("Compte.txt","r",encoding="utf-8") as compte:
            lignes=compte.readlines()

            for el in lignes:
                joueur = el.strip()
                joueur = joueur.split("/")
                if joueur[0] == nom:
                    lignes[lignes.index(el)] = f"{joueur[0]}/{joueur[1]}/{nouveau_solde}\n"

        with open("Compte.txt", "w", encoding="utf-8") as fichier:
            fichier.writelines(lignes)    

    
    #Création de la frame

    frame_jeu_de_des = Frame(fenetre, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_jeu_de_des, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

    
    # Titre
    canva.create_text(200,50,text="Jeu de dés",fill='firebrick',font="Rye 37")

    canva.create_line(400,0,400,750,fill="black",width=2)

    # Affichage des règles

    canva.create_text(200,140, text="Le joueur donne une mise puis lance 3 dés.", fill="gold", font="Limelight 13")
    canva.create_text(200,180, text="Le croupier fait de même.", fill="gold", font="Limelight 13")

    canva.create_text(200,270, text="Si la somme des dés du joueur", fill="gold", font="Limelight 13")
    canva.create_text(200,310, text="est plus élevée que celle du croupier,", fill="gold", font="Limelight 13")

    canva.create_text(200,400, text="il remporte le gain associé à sa mise.", fill="gold", font="Limelight 13")

    canva.create_text(200,490, text="Sinon il perd sa mise.", fill="gold", font="Limelight 13")

    canva.create_text(200,580, text="En cas d'égalité,", fill="gold", font="Limelight 13")
    canva.create_text(200,620, text="le joueur récupère sa mise divisée par 2.", fill="gold", font="Limelight 13")
    
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
    total_banque = canva.create_text(750,270,text=f"Total banque : {0}",fill='gold',font="Limelight 19")
    total_joueur = canva.create_text(750,480,text=f"Total : {0}",fill='gold',font="Limelight 19")


    # Création du bouton quitter

    quitt = Button (canva,text="Quitter",width=30,height=2, bg="red", command=quitter)
    quitt.place(x=1250,y=700)
        


    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)


    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")
    canva.create_text(1350,100,text=f"Solde : {solde_joueur} VTL",font=("Arial",15),fill="white", tags="Solde")


    # Création bouton lancer les dés

    lancer = Button(canva,text="Lancer les dés",width=20,command=jouer)
    lancer.place(x=525,y=400)
        



    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly")
    mise.place(x=800,y=400) 
    mise.current(0)   
    canva.create_text(870,370,text="Mise :",font="Limelight 19",fill="gold")
    


    # Affichage gain total 

    gain = canva.create_text(1300,350,text=f"Gain : {0}",fill='gold',font="Limelight 19")


    return {
        "frame": frame_jeu_de_des,
        "nom_uti": nom,
        "solde_uti": solde_joueur,
    }
