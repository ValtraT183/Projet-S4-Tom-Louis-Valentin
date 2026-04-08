from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*
from Casino.MachineASous.MachineASous_programme import recup_gain, recup_image

from Fonctions_utiles import verif_mise, verif_solde


    



def creerFrameMachineASous(fenetre, fin_jeu, nom, solde, quitter, machineASousToConnexion):
    solde_joueur = int(solde)
 
    def jouer():
        canva.delete("texte")

        if verif_mise(fenetre, solde_joueur, int(mise.get())): #Verif mise
            pass
        else:
            return None

        global case1,case2,case3

        n1 = randint(1,4)
        n2 =randint(1,4)
        n3 =randint(1,4)
        case1 = recup_image(n1)
        case2 = recup_image(n2)
        case3 = recup_image(n3)

        canva.create_image(760,335,image=case1)
        canva.create_image(889,335,image=case2)
        canva.create_image(1017,335,image=case3)

        canva.create_text(900,135,text=f"Gain : {recup_gain(n1,n2,n3,int(mise.get()))} VTL",font="Limelight 28",fill="gold",tags="texte")
        
        return actualiser_solde(recup_gain(n1,n2,n3,int(mise.get())), int(mise.get()))
    
        # Fonction actualiser le solde du joueur dans la frame
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
            canva.after(5000, machineASousToConnexion)

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
    frame_machine_a_sous = Frame(fenetre, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_machine_a_sous, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)



    # Titre

    canva.create_text(220,50,text="Machine à sous",fill='firebrick',font="Rye 37")


    # Barème 

    canva.create_text(100,150,text=f"Barème :",font="Limelight 17",fill="gold")

    img_valentin = Image.open("Image/valentin.png")
    img_valentin = img_valentin.resize((100,125))
    canva.photo_valentin = ImageTk.PhotoImage(img_valentin)
    canva.create_image(100,250,image= canva.photo_valentin)
    canva.create_text(180,250,text="x 3 > 5*Mise",fill="gold",font="Limelight 17",anchor="w")
    canva.create_text(180,275,text="x 2 > 2*Mise",fill="gold",font="Limelight 17",anchor="w")

    
    img_louis = Image.open("Image/louis.png")
    img_louis = img_louis.resize((100,125))
    canva.photo_louis = ImageTk.PhotoImage(img_louis)
    canva.create_image(100,400,image= canva.photo_louis)
    canva.create_text(180,400,text="x 3 > 3*Mise",fill="gold",font="Limelight 17",anchor="w")
    canva.create_text(180,425,text="x 2 > 2*Mise",fill="gold",font="Limelight 17",anchor="w")



    img_tom = Image.open("Image/tom.png")
    img_tom = img_tom.resize((100,125))
    canva.photo_tom = ImageTk.PhotoImage(img_tom)
    canva.create_image(100,550,image=canva.photo_tom)
    canva.create_text(180,550,text="x 3 > 2*Mise",fill="gold",font="Limelight 17",anchor="w")
    canva.create_text(180,575,text="x 2 > 1*Mise",fill="gold",font="Limelight 17",anchor="w")


    canva.create_line(425,0,425,750,width=2)




    # Création de la machine à sous

    canva.machine = PhotoImage(file = "Image/machine.png").subsample(3)
    canva.create_image(900,350,image=canva.machine)


    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")

    canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white", tags="Solde")



    
    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly")
    mise.place(x=500,y=590)    
    mise.current(0)
    canva.create_text(572,570,text="Mise :",font="Limelight 19",fill="gold")
    


    # Création du bouton lancer

    lancer = Button(canva,text=f"Lancer la machine",width=35,height=2,command=jouer)
    lancer.place(x=775,y=580)


    
    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)




    # Création du bouton quitter

    quitter = Button(canva,text="Quitter",width=30,height=2, bg="red", command=quitter)
    quitter.place(x=1250,y=700)

   
  




    return {
        "frame": frame_machine_a_sous,
        "nom_uti": nom,
        "solde_uti": solde,
    }



