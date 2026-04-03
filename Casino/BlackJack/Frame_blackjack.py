from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk 
from random import*
from Casino.Blackjack.Blackjack_programme import*
from time import*

from verif_solde_mise import verif_mise, verif_solde


def creerFrameBlackjack(fenetre, fin_jeu, nom, solde, quitter, blackjackToConnexion):
    solde_joueur = int(solde)


    def commencer_partie():
        global carte_croupier
        global carte_joueur
        global croupier_cache

        canva.delete("texte")

        if verif_mise(fenetre, solde_joueur, int(mise.get())): #Verif mise
            pass
        else:
            return None

        canva.delete("Solde")
        canva.create_text(1350,100,text=f"Solde : {solde_joueur - int(mise.get())} VTL",font=("Arial",15),fill="white",tags="Solde")
        commencer.config(state = DISABLED)
        bouton_tirer.config(state=ACTIVE)
        bouton_rester.config(state=ACTIVE)
        retour.config(state = DISABLED)
        quitt.config(state = DISABLED)

        croupier_cache = True
        carte_croupier = [tirer_cartes(), tirer_cartes()]
        carte_joueur = [tirer_cartes(),tirer_cartes()]

        afficher_carte()
        afficher_score()

        verif_blackjack_initial()



    def verif_blackjack_initial():
        global carte_joueur
        global carte_croupier

        score_j = calcul_score(carte_joueur)
        score_c = calcul_score(carte_croupier)

        if type(score_j) == tuple:
            score_j = max(score_j)
        if type(score_c) == tuple:
            score_c = max(score_c)

        if score_j == 21 and score_c == 21: #égalité
            if len(carte_joueur) == 2 and len(carte_croupier) == 2:
                return afficher_gain(2)
                 

        if score_j == 21 and len(carte_joueur) == 2: #blackjack joueur
            return afficher_gain(3)


        if score_c == 21 and len(carte_croupier) == 2:#blackjack croupier
            return afficher_gain(0)



    def tirer():
        global carte_joueur

        carte_joueur.append(tirer_cartes())
        afficher_carte()
        afficher_score()


        score = calcul_score(carte_joueur)
        if type(score) != tuple:
            verif_21_ou_plus(score,"joueur")

        

    def rester():
        global carte_croupier
        global croupier_cache

        bouton_tirer.config(state=DISABLED)
        bouton_rester.config(state=DISABLED)

        croupier_cache = False
        afficher_carte()
        afficher_score()
        canva.after(2000, jouer_croupier)


    def jouer_croupier():
        global carte_croupier

        score = calcul_score(carte_croupier)
        if type(score) == tuple:
            score = max(score)

        if score <= 16:
            carte_croupier.append(tirer_cartes())
            afficher_carte()
            afficher_score()

            canva.after(2000, jouer_croupier)

        else:
            verif_21_ou_plus(score, "croupier")
            
        

    def verif_21_ou_plus(score,croupier_ou_joueur):
        global carte_croupier
        global carte_joueur

        if croupier_ou_joueur == "croupier":
            if score > 21:
                return afficher_gain(1)
            else:
                return verif_score()
            
        else:
            if score > 21:
                return afficher_gain(0)

            elif score == 21:
                return rester() #Si 21 avec + de 2 cartes, on reste




    def verif_score():
        global carte_croupier
        global carte_joueur

        score_c = calcul_score(carte_croupier)
        score_j = calcul_score(carte_joueur)

        if type(score_c) == tuple:
            score_c = max(score_c)

        if type(score_j) == tuple:
            score_j = max(score_j)
        
        if score_c > score_j:
            return afficher_gain(0)   #le joueur a perdu
        elif score_c == score_j:
            return afficher_gain(2)   # égalité
        else:
            return afficher_gain(1)   # le joueur a gagné
        


    def afficher_gain(win):
        """
        win = 0 --> le joueur a perdu
        win = 1 --> le joueur a gagné
        win = 2 --> égalité
        win = 3 --> Blackjack
        """
        gain = recup_gain(int(mise.get()), win)
        canva.create_text(750,350,text=f"Gain : {gain} VTL",font="Limelight 24",fill="gold",tags="texte")
        if win == 3:
            canva.create_text(750,400, text="BLACKJACK !!", font="Limelight 24", fill = "gold", tags="texte")
        bouton_tirer.config(state=DISABLED)
        bouton_rester.config(state=DISABLED)
        actualiser_solde(gain,int(mise.get()))


    def actualiser_solde(gain, mise):
        nonlocal solde_joueur

        solde_joueur = solde_joueur - mise + gain
        canva.delete("Solde")
        canva.create_text(1350,100,text=f"Solde : {solde_joueur} VTL",font=("Arial",15),fill="white", tags="Solde")

        #On vérifie que le joueur à toujours assez de VTL pour jouer au casino
        if verif_solde(fenetre, solde_joueur, nom):
            pass
        else:
            commencer.config(state=DISABLED)
            retour.config(state=DISABLED)
            canva.after(5000, blackjackToConnexion)

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
        
        canva.after(2000, reset)


    def reset():

        commencer.config(state = ACTIVE)
        retour.config(state = ACTIVE)
        quitt.config(state = ACTIVE)

        canva.delete("resultat")
        canva.delete("score")
        canva.delete("cartes") #on enleve les cartes
        
        pass


    def tirer_cartes():
        liste_cartes = [
        "carreau-2", "carreau-3", "carreau-4", "carreau-5", "carreau-6", "carreau-7",
        "carreau-8", "carreau-9", "carreau-10", "carreau-valet", "carreau-dame", "carreau-roi", "carreau-as",

        "coeur-2", "coeur-3", "coeur-4", "coeur-5", "coeur-6", "coeur-7",
        "coeur-8", "coeur-9", "coeur-10", "coeur-valet", "coeur-dame", "coeur-roi", "coeur-as",

        "trefle-2", "trefle-3", "trefle-4", "trefle-5", "trefle-6", "trefle-7",
        "trefle-8", "trefle-9", "trefle-10", "trefle-valet", "trefle-dame", "trefle-roi", "trefle-as",

        "pique-2", "pique-3", "pique-4", "pique-5", "pique-6", "pique-7",
        "pique-8", "pique-9", "pique-10", "pique-valet", "pique-dame", "pique-roi", "pique-as" 
        ]
       
        return choice(liste_cartes)
    

    def afficher_score():
        global carte_joueur
        global carte_croupier  
        global croupier_cache
        
        canva.delete("score") #On efface les scores affichés

        if croupier_cache:
            croupier = calcul_score([carte_croupier[0]])
        else:
            croupier = calcul_score(carte_croupier)


        joueur = calcul_score(carte_joueur)

        canva.create_text(750,270,text=f"Score Croupier : {croupier}",fill='white',font=("Arial",20), tags="score")
        canva.create_text(750,480,text=f"Votre Score : {joueur}",fill='white',font=("Arial",20), tags="score")
    

    #fonction pour afficher les cartes sur la frame
    def afficher_carte():
        global carte_croupier
        global carte_joueur
        global croupier_cache

        canva.delete("cartes") #On efface les cartes déjà placés
        canva.images = []  #Pour stocker les images

        nb_carte_croupier = len(carte_croupier)
        nb_carte_joueur = len(carte_joueur)

        if nb_carte_croupier > 1:
            ecart_carte_croupier = 280/(nb_carte_croupier-1)
        else:
            ecart_carte_croupier = 0

        ecart_carte_joueur = 280/(nb_carte_joueur-1)
        
        for i,carte in enumerate(carte_croupier):
            if croupier_cache:
                if i == 1:
                    img = recup_image("dos-carte")
                else:
                    img = recup_image(carte)
            else:
                img = recup_image(carte)
            canva.images.append(img)
            canva.create_image(610 + i*ecart_carte_croupier ,175,image=img, tags= "cartes")

        for i,carte in enumerate(carte_joueur):

            img = recup_image(carte)
            canva.images.append(img)
            canva.create_image(610 + i*ecart_carte_joueur ,575,image=img, tags= "cartes")


    #Création de la frame

    frame_blackjack = Frame(fenetre, height=750, width=1500)


    # Création du canva 

    canva = Canvas(frame_blackjack, width=1500, height=750)
    canva.place(x= 0,y=0)


    # Fond de la fenêtre

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)


    # Titre
    canva.create_text(200,50,text="Blackjack",fill='firebrick',font="Rye 37")

    canva.create_line(450,0,450,750,fill="black",width=2)


   
    # Création des tables


    # table du haut

    canva.create_line(550,100,950,100,fill="white",width="2")
    canva.create_line(550,250,950,250,fill="white",width="2")
    canva.create_line(550,100,550,250,fill="white",width="2")
    canva.create_line(950,100,950,250,fill="white",width="2")


    # table du bas 

    canva.create_line(550,650,950,650,fill="white",width="2")
    canva.create_line(550,500,950,500,fill="white",width="2")
    canva.create_line(550,500,550,650,fill="white",width="2")
    canva.create_line(950,500,950,650,fill="white",width="2")

   
    # Affichage du nom de l'utilisateur et du solde

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom}",font=("Arial",15),fill="white")
    canva.create_text(1350,100,text=f"Solde : {solde} VTL",font=("Arial",15),fill="white", tags = "Solde")
    

    # Création du bouton quitter

    quitt = Button(canva,text="Quitter",width=30,height=2,bg="red", command=quitter)
    quitt.place(x=1250,y=700)
        


    # Création du boutton retour au menu 

    retour = Button(canva,text="Retour",width=30,height=2, command=fin_jeu)
    retour.place(x=1250,y=600)


    # Débuter la partie

    commencer = Button(canva,text="Commencer une partie",width=20,command=commencer_partie)
    commencer.place(x=1250,y=400)


    # Création bouton tirer une carte

    bouton_tirer = Button(canva,text="Tirer",width=20,command=tirer, state=DISABLED)
    bouton_tirer.place(x=575,y=700)
        
    # Bouton rester

    bouton_rester = Button(canva,text="Rester",width=20,command=rester, state=DISABLED)
    bouton_rester.place(x=775,y=700)


    # Création menu déroulant pour sélectionner la mise 
    
    liste_mise =[5,10,20,50,100,200,500,1000]
    mise = ttk.Combobox(canva,values=liste_mise,state="readonly",width=21)
    mise.current(0)
    mise.place(x=1250,y=350)    



    # Affichage des règles

    canva.create_text(220,120, text="Le joueur mise puis reçoit deux cartes visibles.", fill="gold", font="Limelight 13")
    
    canva.create_text(220,180, text="Le croupier reçoit aussi deux cartes,", fill="gold", font="Limelight 13")
    canva.create_text(220,200, text="dont une seule est visible.", fill="gold", font="Limelight 13")
    
    canva.create_text(220,260, text="Le but est d'obtenir un total de points",fill="gold", font="Limelight 13")
    canva.create_text(220,280, text="le plus proche possible de 21 sans le dépasser",fill="gold", font="Limelight 13")
    
    canva.create_text(220,340, text="Le joueur peut tirer des cartes", fill="gold", font="Limelight 13")
    canva.create_text(220,360, text="ou s’arrêter quand il le souhaite.", fill="gold", font="Limelight 13")
    canva.create_text(220,380, text="S’il dépasse 21, il perd immédiatement.", fill="gold", font="Limelight 13")
    
    canva.create_text(220,420, text="Ensuite, le croupier joue :", fill="gold", font="Limelight 13")
    canva.create_text(220,440, text="il tire tant que son total est inférieur à 17,", fill="gold", font="Limelight 13")
    canva.create_text(220,460, text="puis s’arrête.", fill="gold", font="Limelight 13")
    canva.create_text(220,480, text="Si le croupier dépasse 21, le joueur gagne. ", fill="gold", font="Limelight 13")

    canva.create_text(220,540, text="Le joueur gagne s’il a un score supérieur,", fill="gold", font="Limelight 13")
    canva.create_text(220,560, text="perd s’il a moins,", fill="gold", font="Limelight 13")
    canva.create_text(220,580, text="et en cas d’égalité, la mise est rendue.", fill="gold", font="Limelight 13")

    canva.create_text(220,640, text="Un blackjack (21 avec deux cartes),", fill="gold", font="Limelight 13")
    canva.create_text(220,660, text="est la meilleure main ", fill="gold", font="Limelight 13")
    canva.create_text(220,680, text="et gagne immédiatement (x3)", fill="gold", font="Limelight 13")
  

    return {
        "frame": frame_blackjack,
        "nom_uti": nom,
        "solde_uti": solde,
    }