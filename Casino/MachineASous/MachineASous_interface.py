from tkinter import*
from PIL import Image, ImageTk 
from random import*
from MachineASous_verifgain import*







# Création des fonctions pour le jeu 



def recup_gain(numero1,numero2,numero3):
    liste_num = [numero1,numero2,numero3]

    occ_de_un = liste_num.count(1)
    occ_de_deux = liste_num.count(2)
    occ_de_trois = liste_num.count(3)

    if occ_de_un == 3 :
        gain = 1000
    elif occ_de_un == 2 :
        gain = 500

    elif occ_de_deux == 3 :
        gain = 500
    elif occ_de_deux == 2 :
        gain = 250
    
    elif occ_de_trois == 3 :
        gain = 100
    elif occ_de_trois == 2 :
        gain = 50

    else :
        gain = 0

    return gain 






def recup_image(numero):
    if numero == 1 :
        img = Image.open("valentin.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
    elif numero == 2:
        img = Image.open("louis.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
    
    else :
        img = Image.open("tom.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)





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
     


   
   
    
# Création de la fenêtre (qui sera une frame par la suite)


fenetre = Tk()
fenetre.title("Machine à sous")
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

canva.create_text(550,50,text="Machine à sous",fill="white",font=("Arial",40))


# Barème 

canva.create_text(100,150,text=f"Barème :",font=("Arial",20),fill="white")

valentin = PhotoImage(file="valentin.png").subsample(15)
canva.create_image(100,250,image=valentin)
canva.create_text(210,250,text="x 3 > 1000 VTL",fill="white",font=("Arial,20"))
canva.create_text(210,275,text="x 2 > 500 VTL  ",fill="white",font=("Arial,20"))

louis = PhotoImage(file="louis.png").subsample(16)
canva.create_image(100,400,image=louis)
canva.create_text(205,400,text="x 3 > 500 VTL",fill="white",font=("Arial,20"))
canva.create_text(205,425,text="x 2 > 250 VTL",fill="white",font=("Arial,20"))

tom = PhotoImage(file="tom.png").subsample(14)
canva.create_image(100,550,image=tom)
canva.create_text(205,550,text="x 3 > 100 VTL",fill="white",font=("Arial,20"))
canva.create_text(205,575,text="x 2 > 50 VTL  ",fill="white",font=("Arial,20"))


canva.create_line(350,0,350,750,width=2)




# Création de la machine à sous

machine = PhotoImage(file = "machine.png").subsample(3)
canva.create_image(900,350,image=machine)


# Affichage du nom de l'utilisateur et du solde

nom_uti = "Moi"
canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")

solde = 20000
canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white")



# Création du boutton lancer

lancer = Button(canva,text="Lancer la roue (400 VTL)",width=35,height=2,command=jouer)
lancer.place(x=775,y=600)



# Création du boutton quitter

quitter = Button(canva,text="Quitter",width=30,height=2)
quitter.place(x=1250,y=700)













fenetre.mainloop()