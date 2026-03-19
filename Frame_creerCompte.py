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



    canva.create_text(400,50, text= "Création du compte", justify=CENTER, fill = "white", font="Arial 50")

    canva.create_text(200,150, text= "Identifiant : ", justify=CENTER, fill = "white", font="Arial 30")
    entree_id = Entry(canva, width= 50)
    entree_id.place(x=650,y=168)

    canva.create_text(200,200, text= "Mot de passe : ", justify=CENTER, fill = "white", font="Arial 30")
    entree_mdp = Entry(canva)
    entree_mdp.place(x=650,y=218)

    canva.create_text(200,250, text= "Age : ", justify=CENTER, fill = "white", font="Arial 30")
    liste_age = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    entree_age = ttk.Combobox(canva, values=liste_age, state="readonly")
    entree_age.place(x=650,y=318)

    
# case à cocher pour les règles de confidentialité 
    etat = BooleanVar()
    politique = Checkbutton(frame_creercompte, text="Veuillez accepter nos règles de confidentialité", variable=etat, font=("Arial 10"))
    politique.place(x= 400,y = 256)



    bouton_creer_compte = Button(canva,text="Créer un nouveau compte", command=valider_nouveau_compte)      
    bouton_valider = Button(canva,text="J'ai déjà un compte", command=retourner)
    bouton_quit = Button(canva, text ="Quitter", command=quitter, bg='red')
    bouton_creer_compte.place(x=500,y=500)
    bouton_valider.place(x=200,y=600)
    bouton_quit.place(x=700,y=600)  



    return {
        "frame": frame_creercompte,
        "id": entree_id,
        "mdp": entree_mdp,
        "age" : entree_age,
        "politique" : etat
    }
