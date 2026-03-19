from tkinter import*
from PIL import Image, ImageTk 
from random import*
from Casino.MachineASous.MachineASous_programme import recup_gain, recup_image



    
# Création de la fenêtre (qui sera une frame par la suite)


def creerFrameMachineASous(parent, fin_jeu, nom, solde, quitter):
    
    def jouer():
        canva.delete("texte")
        global case1,case2,case3

        n1 = randint(1,3)
        n2 =randint(1,3)
        n3 =randint(1,3)
        case1 = recup_image(n1)
        case2 = recup_image(n2)
        case3 = recup_image(n3)

        canva.create_image(760,335,image=case1)
        canva.create_image(889,335,image=case2)
        canva.create_image(1017,335,image=case3)

        canva.create_text(1300,330,text=f"Gain : {recup_gain(n1,n2,n3)} VTL",font=("Arial",25),fill="white",tags="texte")

    #Création de la frame
    frame_connexion = Frame(parent, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_connexion, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)



    # Titre

    canva.create_text(550,50,text="Machine à sous",fill='white',font=("Arial",40))


    # Barème 

    canva.create_text(100,150,text=f"Barème :",font=("Arial",20),fill="white")

    canva.valentin = PhotoImage(file="Image/valentin.png").subsample(15)
    canva.create_image(100,250,image=canva.valentin)
    canva.create_text(210,250,text="x 3 > 1000 VTL",fill="white",font=("Arial,20"))
    canva.create_text(210,275,text="x 2 > 500 VTL  ",fill="white",font=("Arial,20"))

    canva.louis = PhotoImage(file="Image/louis.png").subsample(16)
    canva.create_image(100,400,image=canva.louis)
    canva.create_text(205,400,text="x 3 > 500 VTL",fill="white",font=("Arial,20"))
    canva.create_text(205,425,text="x 2 > 250 VTL",fill="white",font=("Arial,20"))

    canva.tom = PhotoImage(file="Image/tom.png").subsample(14)
    canva.create_image(100,550,image=canva.tom)
    canva.create_text(205,550,text="x 3 > 100 VTL",fill="white",font=("Arial,20"))
    canva.create_text(205,575,text="x 2 > 50 VTL  ",fill="white",font=("Arial,20"))


    canva.create_line(350,0,350,750,width=2)




    # Création de la machine à sous

    canva.machine = PhotoImage(file = "Image/machine.png").subsample(3)
    canva.create_image(900,350,image=canva.machine)


    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")

    canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white")



    # Création du bouton lancer

    lancer = Button(canva,text="Lancer la roue (400 VTL)",width=35,height=2,command=jouer)
    lancer.place(x=775,y=600)



    # Création du bouton quitter

    quitter = Button(canva,text="Quitter",width=30,height=2, command=quitter)
    quitter.place(x=1250,y=700)

    return {
        "frame": frame_connexion,
        "nom_uti": nom,
        "solde_uti": solde,
    }



