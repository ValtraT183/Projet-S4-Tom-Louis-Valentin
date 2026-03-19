from PIL import Image, ImageTk 
from random import*


# Création des fonctions pour le jeu 



def recup_gain(numero1,numero2,numero3,mise):
    liste_num = [numero1,numero2,numero3]

    occ_de_un = liste_num.count(1)
    occ_de_deux = liste_num.count(2)
    occ_de_trois = liste_num.count(3)

    if occ_de_un == 3 :
        gain = 2.5*mise
    elif occ_de_un == 2 :
        gain = 1.25*mise

    elif occ_de_deux == 3 :
        gain = 1.25*mise
    elif occ_de_deux == 2 :
        gain = 0.625*mise
    
    elif occ_de_trois == 3 :
        gain = 0.250*mise
    elif occ_de_trois == 2 :
        gain = 0.125*mise

    else :
        gain = 0

    return gain 






def recup_image(numero):
    if numero == 1 :
        img = Image.open("Image/valentin.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
        
    elif numero == 2:
        img = Image.open("Image/louis.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
    
    else :
        img = Image.open("Image/tom.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)





     
