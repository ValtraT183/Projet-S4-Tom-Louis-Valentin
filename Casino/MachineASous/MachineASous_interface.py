from tkinter import*
from PIL import Image, ImageTk 



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

canva.create_text(550,50,text="Machine à sous",fill='white',font=("Arial",40))


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

lancer = Button(canva,text="Lancer la roue (400 VTL)",width=35,height=2)
lancer.place(x=775,y=600)










fenetre.mainloop()