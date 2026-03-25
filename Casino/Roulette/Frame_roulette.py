from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*
from time import*
from Casino.Roulette.Roulette_programme import *








def creerFrameRoulette(fenetre, fin_jeu, nom, solde, quitter):
    
    def jouer() :
        start_time = perf_counter()
        
        def animation(coordonnees):

            canva.bille_img = PhotoImage(file="Image/bille.png").subsample(25)
            
            chemin = creation_chemin()
            xdebut = coordonnees[chemin[0]][0]
            ydebut = coordonnees[chemin[0]][1] 
            bille = canva.create_image(xdebut,ydebut,image=canva.bille_img)

            def deplacer(i):
                if i >= len(chemin):
                    end_time= perf_counter()
                    print(f"{end_time-start_time}s")
                    return
            
                x = coordonnees[chemin[i]][0]
                y = coordonnees[chemin[i]][1]
                
                canva.coords(bille, x, y)
                
                ecart = randint(1,3)
                canva.after(50,lambda:deplacer(i+ecart))
                
                
            deplacer(0)

        animation(case_coordonnees)
        
        
        
            




    #Création de la frame
    frame_roulette = Frame(fenetre, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_roulette, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)



    # Titre

    canva.create_text(550,50,text="Roulette",fill='white',font=("Arial",40))


    # Barème 

    canva.create_text(100,150,text=f"Barème :",font=("Arial",20),fill="white")
    canva.create_line(350,0,350,750,width=2)




    # Création de la roulette

    canva.machine = PhotoImage(file = "Image/roulette.png")
    canva.create_image(900,350,image=canva.machine)


    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")

    canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white")




    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly")
    mise.place(x=500,y=590)    
    mise.current(0)
    canva.create_text(570,570,text="Mise :",font=("Arial",15),fill="white") 
    

    
    # Création menu déroulant pour sélectionner le numéro
    
    liste_numero =[i for i in range(37)]
    mise = ttk.Combobox(canva,values=liste_numero,state="readonly")
    mise.place(x=1250,y=400)    
    canva.create_text(570,570,text="Mise :",font=("Arial",15),fill="white") 


        
    # Création menu déroulant pour sélectionner la couleur
    
    liste_numero =["Rouge","Noir"]
    mise = ttk.Combobox(canva,values=liste_numero,state="readonly")
    mise.place(x=1250,y=200)    
    canva.create_text(570,570,text="Mise :",font=("Arial",15),fill="white") 


            
    # Création menu déroulant pour sélectionner la parité
    
    liste_numero =["Pair","Impair"]
    mise = ttk.Combobox(canva,values=liste_numero,state="readonly")
    mise.place(x=1250,y=500)    
    canva.create_text(570,570,text="Mise :",font=("Arial",15),fill="white") 





    # Création du bouton lancer

    lancer = Button(canva,text=f"Lancer la roue",width=35,height=2,command=jouer)
    lancer.place(x=775,y=580)



    


    
    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)






    # Création du bouton quitter

    quitter = Button(canva,text="Quitter",width=30,height=2, command=quitter)
    quitter.place(x=1250,y=700)


    return {
        "frame": frame_roulette,
        "nom_uti": nom,
        "solde_uti": solde,
    }



