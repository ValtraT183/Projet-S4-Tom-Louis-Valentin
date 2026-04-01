from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*

from Casino.Roulette.Roulette_programme import *





def creerFrameRoulette(fenetre, fin_jeu, nom, solde, quitter):
    
    solde_joueur = int(solde)


    def jouer() :
        canva.delete("texte")
        canva.delete("Solde")
        canva.create_text(1350,100,text=f"Solde : {solde_joueur - int(mise.get())} VTL",font=("Arial",15),fill="white",tags="Solde")

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
            quitt.config(state="disabled")
            retour.config(state="disabled")
           
            def deplacer(i):
                global derniere_case_affichee
                if i >= len(chemin):
                    gain = recup_gain(int(mise.get()), selection["valeur"], case_numero_et_couleur[derniere_case_affichee])
                    canva.create_text(900,100,text=f"Gain : {gain} VTL",font="Limelight 24",fill="gold",tags="texte")
                    lancer.config(state="normal")
                    mise.config(state="normal")
                    numero.config(state="normal")
                    rouge.config(state="normal")
                    noir.config(state="normal")
                    pair.config(state="normal")
                    impair.config(state="normal")
                    quitt.config(state="normal")
                    retour.config(state="normal")
                
                    return actualiser_solde(gain, int(mise.get()))
            
                x = coordonnees[chemin[i]][0]
                y = coordonnees[chemin[i]][1]
                derniere_case_affichee = chemin[i]
                canva.coords(bille, x, y)
                
                ecart = randint(1,3)
                canva.after(50,lambda:deplacer(i+ecart))
                
                
            deplacer(0)
        
        animation(case_coordonnees)

        
    # Fonction actualiser le solde du joueur dans la frame
    def actualiser_solde(gain, mise):
        nonlocal solde_joueur

        solde_joueur = solde_joueur - mise + gain
        canva.delete("Solde")
        canva.create_text(1350,100,text=f"Solde : {solde_joueur} VTL",font=("Arial",15),fill="white", tags="Solde")

        actualiser_solde_txt(solde_joueur, nom)

    # Fonction actualiser le solde dans le txt

    def actualiser_solde_txt(nouveau_solde, nom):
        global solde_courant
        solde_courant = nouveau_solde
        lignes=[]

        with open("Compte.txt","r",encoding="utf-8") as compte:
            lignes=compte.readlines()

            for el in lignes:
                joueur = el.strip()
                joueur = joueur.split("/")
                if joueur[0] == nom:
                    lignes[lignes.index(el)] = f"{joueur[0]}/{joueur[1]}/{nouveau_solde}\n"

        with open("Compte.txt", "w", encoding="utf-8") as fichier:
            fichier.writelines(lignes) 
        
    
        

    
    
    def afficher_selection() :
        canva.delete("texte")
        if selection["type"] == None :
            texte = "Aucune sélection"
            lancer.config(state="disabled")
        else :
            texte = f"Votre sélection : {selection["valeur"]}"
            lancer.config(state="active")

        canva.create_text(200,725,text=texte,font="Limelight 17",fill="gold",tag="texte")



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

    canva.create_text(220,50,text="Roulette",fill='firebrick',font="Rye 37")
    canva.create_line(425,0,425,750,width=2)
    canva.create_line(0,375,425,375,width=2)




# ---------------------------------Affichage des règles------------------------------------------------

    canva.create_text(215,130, text="Le joueur choisit un pari et une mise.",fill="gold",font="Limelight 13")
    canva.create_text(215,180, text="La bille est lancée dans la roulette.",fill="gold",font="Limelight 13")
    canva.create_text(215,230, text="Si le résultat correspond à son choix,",fill="gold",font="Limelight 13")
    canva.create_text(215,260, text="il gagne selon le barème.",fill="gold",font="Limelight 13")
    canva.create_text(215,310, text="Sinon, il perd sa mise.",fill="gold",font="Limelight 13")


# -----------------------------------------------------------------------------------------------------
    






# --------------------------------------Sélection------------------------------------------------------

    canva.create_text(100,425,text=f"Couleur :",font="Limelight 17",fill="gold")
    canva.create_text(100,450, text="(x2)",fill="gold",font="Limelight 13")

    canva.create_text(100,525,text=f"Parité :",font="Limelight 17",fill="gold")
    canva.create_text(100,550, text="(x2)",fill="gold",font="Limelight 13")

    canva.create_text(100,625,text=f"Numéro :",font="Limelight 17",fill="gold")
    canva.create_text(100,650, text="(x30)",fill="gold",font="Limelight 13")

   
    # Création menu déroulant pour sélectionner le numéro
    
    liste_numero =[i for i in range(37)]
    numero = ttk.Combobox(canva,values=liste_numero,state="readonly",width=26)
    numero.place(x=200,y=615) 
    numero.bind("<<ComboboxSelected>>", choix_numero)   
    

        
    # Création boutons pour sélectionner la couleur
    
    rouge = Button(canva,text="Rouge",width=10,height=2,command=r)
    rouge.place(x=200,y=405)
    

    noir = Button(canva,text="Noir",width=10,height=2,command=n)
    noir.place(x=300,y=405)


            
    # Création boutons pour sélectionner la parité

    pair = Button(canva,text="Pair",width=10,height=2,command=pai)
    pair.place(x=200,y=505)

    impair = Button(canva,text="Impair",width=10,height=2,command=imp)
    impair.place(x=300,y=505)


# -----------------------------------------------------------------------------------------------------

    # Création de la roulette

    canva.machine = PhotoImage(file = "Image/roulette.png")
    canva.create_image(900,350,image=canva.machine)



    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")

    canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white", tags="Solde")




    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly")
    mise.place(x=500,y=590)    
    mise.current(0)
    canva.create_text(570,570,text="Mise :",font="Limelight 17",fill="gold") 
    

 
    # Création du bouton lancer

    lancer = Button(canva,text=f"Lancer la roue",width=35,height=2,command=jouer)
    lancer.place(x=775,y=580)


    afficher_selection()  # Pour avoir le message : "Aucune sélection"


   
    

    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)


    # Création du bouton quitter

    quitt = Button(canva,text="Quitter",width=30,height=2,bg="red", command=quitter)
    quitt.place(x=1250,y=700)




    return {
        "frame": frame_roulette,
        "nom_uti": nom,
        "solde_uti": solde,
    }



