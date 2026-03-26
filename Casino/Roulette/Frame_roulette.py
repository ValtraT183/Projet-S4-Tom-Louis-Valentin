from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*

from Casino.Roulette.Roulette_programme import *




global indice_case_fin
global case_fin     # liste 


def creerFrameRoulette(fenetre, fin_jeu, nom, solde, quitter):
    
    def jouer() :
        canva.delete("texte")
        
        def animation(coordonnees):
            
            canva.bille_img = PhotoImage(file="Image/bille.png").subsample(25)
            
            chemin = creation_chemin()
            xdebut = coordonnees[chemin[0]][0]
            ydebut = coordonnees[chemin[0]][1] 
            bille = canva.create_image(xdebut,ydebut,image=canva.bille_img)
            afficher_selection()
            lancer.config(state="disabled")
            mise.config(state="disabled")
            numero.config(state="disabled")
            rouge.config(state="disabled")
            noir.config(state="disabled")
            pair.config(state="disabled")
            impair.config(state="disabled")
           
            def deplacer(i):
                global derniere_case_affichee
                if i >= len(chemin):
                    gain = recup_gain(int(mise.get()), selection["valeur"], case_numero_et_couleur[derniere_case_affichee])
                    canva.create_text(500,350,text=f"Gain : {gain} VTL",font=("Arial",25),fill="white",tags="texte")
                    lancer.config(state="active")
                    mise.config(state="active")
                    numero.config(state="active")
                    rouge.config(state="active")
                    noir.config(state="active")
                    pair.config(state="active")
                    impair.config(state="active")
                
                    return
            
                x = coordonnees[chemin[i]][0]
                y = coordonnees[chemin[i]][1]
                derniere_case_affichee = chemin[i]
                canva.coords(bille, x, y)
                
                ecart = randint(1,3)
                canva.after(50,lambda:deplacer(i+ecart))
                
                
            deplacer(0)
        
        animation(case_coordonnees)
        
        
    
        

    
    
    def afficher_selection() :
        canva.delete("texte")
        if selection["type"] == None :
            texte = "Aucune sélection"
        else :
            texte = f"Votre sélection : {selection["valeur"]}"

        canva.create_text(300,150,text=texte,font=("Arial",15),fill="white",tag="texte")



    def pai():
        selection["type"] = "Parité"
        selection["valeur"] = "Pair"
        afficher_selection()

    def imp() :
        selection["type"] = "Parité"
        selection["valeur"] = "Impair"
        afficher_selection()

    def r():
        selection["type"] = "Couleur"
        selection["valeur"] = "Rouge"
        afficher_selection()

    def n():
        selection["type"] = "Couleur"
        selection["valeur"] = "Noir"
        afficher_selection()
    
    def choix_numero(_):
        selection["type"] = "Numéro"
        selection["valeur"] = int(numero.get())
        afficher_selection()

    
        


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
    numero = ttk.Combobox(canva,values=liste_numero,state="readonly")
    numero.place(x=1250,y=400) 
    numero.bind("<<ComboboxSelected>>", choix_numero)   
    

        
    # Création boutons pour sélectionner la couleur
    
    rouge = Button(canva,text="Rouge",width=10,height=2,command=r)
    rouge.place(x=1200,y=150)
    

    noir = Button(canva,text="Noir",width=10,height=2,command=n)
    noir.place(x=1200,y=300)


            
    # Création boutons pour sélectionner la parité

    pair = Button(canva,text="Pair",width=10,height=2,command=pai)
    pair.place(x=1200,y=450)

    impair = Button(canva,text="Impair",width=10,height=2,command=imp)
    impair.place(x=1200,y=600)




    



    # Création du bouton lancer

    lancer = Button(canva,text=f"Lancer la roue",width=35,height=2,command=jouer)
    lancer.place(x=775,y=580)


    afficher_selection()  # Pour avoir le message : Aucune sélection



    


    
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



