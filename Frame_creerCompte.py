from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk



def creerFrameCreerCompte(parent, retourner, valider_nouveau_compte, quitter):
 
    # Création de la frame
    frame_creercompte = Frame(parent, height=750, width=1500) 

    # Création du canva
    canva = Canvas(frame_creercompte, height=750, width=1500)
    canva.pack()

    # Fond de la fenêtre
    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

    # Titre
    canva.titre = PhotoImage(file="Image/titre.png").subsample(2)
    canva.create_image(750,100,image = canva.titre)





# Création des textes
# --------------------------------------------------------------------------------------------

    canva.create_text(240,100, text= "Création du compte", justify=CENTER, fill = "firebrick", font="Rye 31")

    canva.create_text(200,250, text= "Identifiant : ", justify=CENTER, fill = "gold", font="Limelight 27")
    entree_id = Entry(canva, width= 50)
    entree_id.place(x=550,y=242)

    canva.create_text(200,350, text= "Mot de passe : ", justify=CENTER, fill = "gold", font="Limelight 27")
    entree_mdp = Entry(canva, width = 50)
    entree_mdp.place(x=550,y=342)

    canva.create_text(200,450, text= "Age : ", justify=CENTER, fill = "gold", font="Limelight 27")
    liste_age = [i for i in range(1,101)]
    entree_age = ttk.Combobox(canva, width = 47,values=liste_age, state="readonly")
    entree_age.place(x=550,y=442)

# --------------------------------------------------------------------------------------------





    
# Création des Entry
# --------------------------------------------------------------------------------------------

    etat = BooleanVar()
    politique = Checkbutton(frame_creercompte, text="Veuillez accepter nos règles de confidentialité", variable=etat, font=("Arial 10"))
    politique.place(x=800, y=500)


    bouton_creer_compte = Button(canva,text="Créer un nouveau compte", command=valider_nouveau_compte,width=30,height=2)      
    bouton_valider = Button(canva,text="J'ai déjà un compte", command=retourner,width=30,height=2)
    bouton_quit = Button(canva, text ="Quitter", command=quitter,width=30,height=2,bg="red")
    bouton_creer_compte.place(x=425,y=600)
    bouton_valider.place(x=800,y=600)
    bouton_quit.place(x=1250,y=700)  

# --------------------------------------------------------------------------------------------



    return {
        "frame": frame_creercompte,
        "id": entree_id,
        "mdp": entree_mdp,
        "age" : entree_age,
        "politique" : etat
    }
