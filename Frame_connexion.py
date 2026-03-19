from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from CreerCompte import creerFrameCreerCompte


# fonction


def creerFrameConnexion(parent,valider,creercompte,quitter):

    # Création de la frame
    frame_connexion = Frame(parent, height=750, width=1500)

    # Création du canva
    canva = Canvas(frame_connexion, height=750, width=1500)
    canva.pack()
    # Fond de la fenêtre

    image = Image.open("Casino/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

    # Titre
    canva.titre = PhotoImage(file="Casino/titre.png").subsample(2)
    canva.create_image(750,100,image = canva.titre)



    canva.create_text(400,50, text= "Connexion", justify=CENTER, fill = "white", font="Arial 50")

    canva.create_text(200,200, text= "Identifiant : ", justify=CENTER, fill = "white", font="Arial 30")
    entree_id = Entry(parent, width= 50)
    entree_id.place(x=650,y=200)


    canva.create_text(200,250, text= "Mot de passe : ", justify=CENTER, fill = "white", font="Arial 30")
    entree_mdp = Entry(parent,show="*")
    entree_mdp.place(x=650,y=250)



    bouton_creer_compte = Button(parent,text="Créer un nouveau compte",command=creercompte)        #CHANGER DE FRAME
    bouton_valider = Button(parent,text="Se connecter", command=valider)
    bouton_quit = Button(parent, text ="Quitter", command=quitter, bg='red')
    bouton_creer_compte.place(x=500,y=500)
    bouton_valider.place(x=200,y=600)
    bouton_quit.place(x=700,y=600)  

    return {
        "frame": frame_connexion,
        "id": entree_id,
        "mdp": entree_mdp,
        
    }
