from PIL import Image, ImageTk 






# Fonction récuperer gain
# -------------------------------------------------------------------------------------------

def recup_gain(numero1,numero2,numero3,mise):
    liste_num = [numero1,numero2,numero3,]

    occ_de_un = liste_num.count(1)
    occ_de_deux = liste_num.count(2)
    occ_de_trois = liste_num.count(3)

    if occ_de_un == 3 :
        gain = 5*mise
    elif occ_de_un == 2 :
        gain = 2*mise

    elif occ_de_deux == 3 :
        gain = 3*mise
    elif occ_de_deux == 2 :
        gain = 2*mise
    
    elif occ_de_trois == 3 :
        gain = mise*2
    elif occ_de_trois == 2 :
        gain = mise

    else :
        gain = 0

    return gain

# -------------------------------------------------------------------------------------------









# Fonction ouvrir image (et conversion)
# -------------------------------------------------------------------------------------------

def recup_image(numero):
    if numero == 1 :
        img = Image.open("Image/valentin.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
        
    elif numero == 2:
        img = Image.open("Image/louis.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
    
    elif numero == 3 :
        img = Image.open("Image/tom.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)
    else :
        img = Image.open("Image/rien.png")
        img = img.resize((114,170))
        return ImageTk.PhotoImage(img)

# -------------------------------------------------------------------------------------------





     