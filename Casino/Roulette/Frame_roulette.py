from tkinter import*
from PIL import Image, ImageTk 








def creerFrameMachineASous(fenetre, fin_jeu, nom, solde, quitter):
    
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
