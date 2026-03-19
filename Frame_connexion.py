from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




def creerFrameConnexion(parent,valider,quitter):

    # Création de la frame
    frame_connexion = Frame(parent, height=750, width=1500)

    # Création du canva
    canva = Canvas(frame_connexion, height=750, width=1500)
    canva.pack()
    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

    # Titre
    canva.titre = PhotoImage(file="Image/titre.png").subsample(2)
    canva.create_image(750,100,image = canva.titre)



    canva.create_text(200,100, text= "Connexion", justify=CENTER, fill = "firebrick", font="Rye 50")

    canva.create_text(200,300, text= "Identifiant : ", justify=CENTER, fill = "gold", font="Limelight 27")
    entree_id = Entry(parent, width= 50)
    entree_id.place(x=550,y=300)


    canva.create_text(200,400, text= "Mot de passe : ", justify=CENTER, fill = "gold", font="Limelight 27")
    entree_mdp = Entry(parent, width=50,show="*")
    entree_mdp.place(x=550,y=400)



    bouton_creer_compte = Button(parent,text="Créer un nouveau compte",padx=20,pady=10)        #CHANGER DE FRAME
    bouton_valider = Button(parent,text="Se connecter", command=valider,padx=20,pady=10)
    bouton_quit = Button(parent, text ="Quitter", command=quitter, bg='red',padx=20,pady=10)
    bouton_creer_compte.place(x=525,y=500)
    bouton_valider.place(x=800,y=500)
    bouton_quit.place(x=1250,y=600)  

    return {
        "frame": frame_connexion,
        "id": entree_id,
        "mdp": entree_mdp,
    }
