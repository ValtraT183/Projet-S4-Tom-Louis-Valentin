from tkinter import *
from PIL import Image, ImageTk 

# Création de la fenêtre

fenetre = Tk()
fenetre.title("Casino")
fenetre.iconbitmap("casinologo.ico")
fenetre.geometry("1500x750")

# Création du canva 

canva = Canvas(fenetre, width=1500, height=750)
canva.place(x= 0,y=0)


# Fond de la fenêtre

image = Image.open("background.png")
image = image.resize((1500, 750))
photo_background = ImageTk.PhotoImage(image)
canva.create_image(0, 0, anchor=NW, image=photo_background)


# Titre

titre = PhotoImage(file="titre.png").subsample(2)
canva.create_image(750,100,image = titre)


# Création des boutons

blackjack = Button(canva,text = "BlackJack",width=50,height=2)
blackjack.place(x=580,y=250)

machine = Button(canva,text="Machine à sous",width=50,height=2)
machine.place(x=580,y=350)

roulette = Button(canva,text="Roulette",width=50,height=2)
roulette.place(x=580,y=450)

roulette = Button(canva,text="Roulette",width=50,height=2)
roulette.place(x=580,y=450)

des = Button(canva,text="Jeu de dés",width=50,height=2)
des.place(x=580,y=550)

quitter = Button(canva,text="Quitter",width=30,height=2)
quitter.place(x=1250,y=700)



# Affichage du nom de l'utilisateur et du solde

nom_uti = "Moi"
canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")

solde = 20000
canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white")









fenetre.mainloop()