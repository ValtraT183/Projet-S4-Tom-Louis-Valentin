from tkinter import*
from PIL import Image, ImageTk 
from random import*






def creerFrameJeuDeDes(parent, fin_jeu, nom, solde, quitter):

    #Création de la frame

    frame_jeu_de_des = Frame(parent, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_jeu_de_des, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)



    # Titre
    canva.create_text(550,50,text="Machi",fill='white',font=("Arial",40))


    def recup_image(numero):
        img = Image.open(f"face{numero}.png")
        img = img.resize((50,50))
        return ImageTk.PhotoImage(img)


    def jouer():
        global de1,de2,de3,de1a,de2a,de3a

        canva.delete("des")

        n1, n2, n3 = randint(1,6), randint(1,6), randint(1,6)
        n1a, n2a, n3a = randint(1,6), randint(1,6), randint(1,6)

        de1 = recup_image(n1)
        de2 = recup_image(n2)
        de3 = recup_image(n3)

        de1a = recup_image(n1a)
        de2a = recup_image(n2a)
        de3a = recup_image(n3a)

        # joueur du haut
        canva.create_image(350,200,image=de1, tags="des")
        canva.create_image(500,200,image=de2, tags="des")
        canva.create_image(650,200,image=de3, tags="des")

        # joueur du bas
        canva.create_image(350,550,image=de1a, tags="des")
        canva.create_image(500,550,image=de2a, tags="des")
        canva.create_image(650,550,image=de3a, tags="des")



        # Création du bouton quitter

        quitter = Button(canva,text="Quitter",width=30,height=2, command=quitter)
        quitter.place(x=1250,y=700)
        
        
        
    return {
        "frame": frame_jeu_de_des,
        "nom_uti": nom,
        "solde_uti": solde,
    }