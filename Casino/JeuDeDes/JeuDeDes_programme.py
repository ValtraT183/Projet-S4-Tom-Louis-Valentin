# Programme Jeu de Dé Projet Casino S4

from random import*
from tkinter import *
from PIL import Image, ImageTk 

# CONSTANTES
VTL_DEPART = 100
MISE_MIN = 5
NB_DES = 3


# FONCTIONS DU JEU
def lancer_des(nombre_de_des):
    return[random.randint(1,6) for _ in range(nombre_de_des)]

def calculer_somme(liste_des):
    return sum(liste_des)

def determiner_resultat(somme_joueur, somme_croupier):
    if somme_joueur > somme_croupier:
        return "Victoire"
    elif somme_joueur < somme_croupier:
        return "Defaite"
    else :
        return "Egalité"
    
def calculer_gain(mise, resultat_du_tour):
    if resultat_du_tour == "Victoire":
        return mise
    elif resultat_du_tour == "Defaite":
        return -mise
    else :
        return 0




def recup_image(numero):

    if numero == 1 :
        img = Image.open("face1.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    
    elif numero == 2 :
        img = Image.open("face2.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    

    elif numero == 3 :
        img = Image.open("face3.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    

    elif numero == 4 :
        img = Image.open("face4.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    

    elif numero == 5 :
        img = Image.open("face5.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    

    else  :
        img = Image.open("face6.png")
        img = img.resize((100,75))
        return ImageTk.PhotoImage(img)
    
    


def recup_gain(mise):
    tot = n1+n2+n3
    tota = n1a+n2a+n3a
    
    if tot > tota :
        return 2*mise
    
    elif tot==tota :
        return mise
    
    else : 
        return 0






def jouer() :
    canva.delete("total")
    canva.delete("gain")

    global de1,de2,de3,de1a,de2a,de3a
    global n1,n2,n3,n1a,n2a,n3a



    n1 = randint(1,6)               
    n2 = randint(1,6)
    n3 = randint(1,6)
    n1a = randint(1,6)
    n2a = randint(1,6)
    n3a = randint(1,6)


    de1 = recup_image(n1)
    de2 = recup_image(n2)
    de3 = recup_image(n3)
    de1a= recup_image(n1a)
    de2a= recup_image(n2a)
    de3a= recup_image(n3a)


    canva.create_image(650,150,image=de1)
    canva.create_image(750,240,image=de2)
    canva.create_image(850,150,image=de3)

    canva.create_image(650,500,image=de1a)
    canva.create_image(750,590,image=de2a)
    canva.create_image(850,500,image=de3a)


    canva.create_text(200,200,text=f"Total : {n1a+n2a+n3a} ",font=("Arial",25),fill="white",tags="total")
    canva.create_text(1300,550,text=f"Total : {n1+n2+n3} ",font=("Arial",25),fill="white",tags="total")
    canva.create_text(750,375,text=f"Gain : {recup_gain(5)}",font=("Arial",25),fill="white",tags="gain")   # faire menu déroulant pour récuperer la mise
     
    




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



# Création des tables 
  
# bas 
canva.create_line(550,650,950,650,width=2,fill="white")
canva.create_line(550,450,950,450,width=2,fill="white")
canva.create_line(550,450,550,650,width=2,fill="white")
canva.create_line(950,450,950,650,width=2,fill="white")


# haut
canva.create_line(550,100,950,100,width=2,fill="white")
canva.create_line(550,300,950,300,width=2,fill="white")
canva.create_line(550,100,550,300,width=2,fill="white")
canva.create_line(950,100,950,300,width=2,fill="white")




# Création bouton lancer les des


lancer = Button(canva,text="Lancer les dés",width=30,height=2,command=jouer)
lancer.place(x=1200,y=325)



# Création menu déroulant pour modifier la mise 

mise = Button(canva,text="Modifier la mise",width=30,height=2)
mise.place(x=1200,y=375)




# Affichage du nom de l'utilisateur et du solde

nom_uti = "Moi"
canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")

solde = 20000
canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white")



fenetre.mainloop()
