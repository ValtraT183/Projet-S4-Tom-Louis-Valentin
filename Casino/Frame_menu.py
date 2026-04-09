from tkinter import *
from PIL import Image, ImageTk 
from random import*


# Fonction créer frame menu
# -------------------------------------------------------------------------------------------

def creerFrameMenu(parent, retourner, nom_uti, solde_uti, quitter, creerMachineASous, creerJeuDeDes, creerBlackjack, creerRoulette):
    






# Fonction affichage de la Newsletter
# -------------------------------------------------------------------------------------------

    def affichageNewsletter(liste):
        canva.delete("newsletter")
        info = randint(0,len(liste)-1)
        all_texte = liste[info]
       
        if info == 0 :

            texte1 = all_texte[0:19]
            texte2 = all_texte[20:]

            canva.create_text(140,250,text=texte1,font=("Arial",18),fill="white",tags="newsletter",anchor=W)
            canva.create_text(175,350,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)

            canva.after(10000,lambda :affichageNewsletter(liste))
       
        elif info == 1 :
             
             texte1 = all_texte[:37]
             texte2 = all_texte[38:]
             
             canva.create_text(68,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
             canva.create_text(147,310,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)

             canva.after(10000,lambda :affichageNewsletter(liste))

        elif info == 2 :
             
             texte1 = all_texte[:41]
             texte2 = all_texte[41:52]
             texte3 = all_texte[52:]
             
             canva.create_text(58,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
             canva.create_text(187,310,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
             canva.create_text(65,370,text=texte3,font=("Arial",15),fill="white",tags="newsletter",anchor=W)

             canva.after(10000,lambda :affichageNewsletter(liste))

        elif info == 3 :
            
            texte1 = all_texte[:30]
            texte2 = all_texte[31:55]
            texte3 = all_texte[56:72]
            texte4 = all_texte[73:92]
            texte5 = all_texte[93:103]
            texte6 = all_texte[104:132]
            texte7 = all_texte[133:156]
            texte8 = all_texte[157:]
            
            canva.create_text(53,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(85,280,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,340,text=texte3,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,370,text=texte4,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,400,text=texte5,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(62,500,text=texte6,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(90,530,text=texte7,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(35,560,text=texte8,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
           
            canva.after(10000,lambda :affichageNewsletter(liste))

        elif info == 4 :
            
            texte1 = all_texte[:21]
            texte2 = all_texte[22:60]
            texte3 = all_texte[61:73]
            texte4 = all_texte[74:]
            
            canva.create_text(130,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(55,280,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(170,340,text=texte3,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(85,370,text=texte4,font=("Arial",15),fill="white",tags="newsletter",anchor=W)

            canva.after(10000,lambda :affichageNewsletter(liste))

        elif info == 5 :
                        
            texte1 = all_texte[:25]
            texte2 = all_texte[26:51]
            texte3 = all_texte[52:91]
            texte4 = all_texte[92:]
            
            canva.create_text(105,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(120,310,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(50,400,text=texte3,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(185,460,text=texte4,font=("Arial",15),fill="white",tags="newsletter",anchor=W)

            canva.after(10000,lambda :affichageNewsletter(liste))
        

        else :

            texte1 = all_texte[:9]
            texte2 = all_texte[10:21]
            texte3 = all_texte[22:33]
            texte4 = all_texte[34:63]
            texte5 = all_texte[64:]
            
            canva.create_text(185,250,text=texte1,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,310,text=texte2,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,340,text=texte3,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(53,370,text=texte4,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            canva.create_text(150,430,text=texte5,font=("Arial",15),fill="white",tags="newsletter",anchor=W)
            
            canva.after(10000,lambda :affichageNewsletter(liste))

# -------------------------------------------------------------------------------------------









# Fonction récuperer l'indice du solde le plus haut dans le txt
# -------------------------------------------------------------------------------------------

    def indiceSoldeLePlusHaut():
        with open("Compte.txt","r",encoding="utf8") as compte :
            lignes = compte.readlines()
            soldes = []
            for ligne in lignes :
                liste = ligne.strip().split("/")
                soldes.append(int(liste[2])) 
            haut = soldes[0]
            indice=0
            for i in range(len(soldes)):
                if soldes[i] > haut :
                    indice = i
                    haut = soldes[i]

            return indice

# -------------------------------------------------------------------------------------------








# Fonction récuperer le nom de l'utilisateur qui a le plus haut solde et son solde 
# -------------------------------------------------------------------------------------------

    def nomSoldeUtiStar(indice) :
        with open("Compte.txt","r",encoding="utf8") as compte :
            lignes = compte.readlines()
            info_joueur = lignes[indice].strip().split("/")
            return (info_joueur[0],info_joueur[2])
        
# -------------------------------------------------------------------------------------------







    
    # Création de la frame
# -------------------------------------------------------------------------------------------

    frame_menu = Frame(parent, width=1500, height=750)

# -------------------------------------------------------------------------------------------






    # Création du canva
# -------------------------------------------------------------------------------------------

    canva = Canvas(frame_menu, width=1500, height=750)
    canva.pack()

# -------------------------------------------------------------------------------------------






    # Fond de la fenêtre
# -------------------------------------------------------------------------------------------

    image = Image.open("Image/background.png")
    image = image.resize((1500, 750))
    canva.photo_background = ImageTk.PhotoImage(image)
    canva.create_image(0, 0, anchor=NW, image=canva.photo_background)

# -------------------------------------------------------------------------------------------







    # Titre
# -------------------------------------------------------------------------------------------

    canva.titre = PhotoImage(file="Image/titre.png").subsample(2)
    canva.create_image(750,100,image = canva.titre)

# -------------------------------------------------------------------------------------------








    # Création du boutton blackjack
# -------------------------------------------------------------------------------------------

    blackjack = Button(canva,text = "BlackJack",width=50,height=2, command=creerBlackjack)
    blackjack.place(x=580,y=250)

# -------------------------------------------------------------------------------------------







    # Création du boutton machine à sous
# -------------------------------------------------------------------------------------------

    machine = Button(canva,text="Machine à sous",width=50,height=2, command=creerMachineASous)
    machine.place(x=580,y=350)
# -------------------------------------------------------------------------------------------








   # Création du boutton roulette
# -------------------------------------------------------------------------------------------

    roulette = Button(canva,text="Roulette",width=50,height=2, command=creerRoulette)
    roulette.place(x=580,y=450)

# -------------------------------------------------------------------------------------------








# Création du boutton machine à dés
# -------------------------------------------------------------------------------------------

    des = Button(canva,text="Jeu de dés",width=50,height=2, command=creerJeuDeDes)
    des.place(x=580,y=550)

# -------------------------------------------------------------------------------------------







    
    # Création du boutton se déconnecter
# -------------------------------------------------------------------------------------------

    retour = Button(canva, text="Se déconnecter", width=30, height=2, command=retourner)
    retour.place(x=1250, y=600)

# -------------------------------------------------------------------------------------------









    # Création du boutton quitter
# -------------------------------------------------------------------------------------------

    quitt = Button(canva,text="Quitter",width=30,height=2,bg="red", command=quitter)
    quitt.place(x=1250,y=700)

# -------------------------------------------------------------------------------------------







    # Affichage du nom de l'utilisateur et du solde
# -------------------------------------------------------------------------------------------

    canva.create_text(1350,50,text=f"Nom d'utilisateur : {nom_uti}",font=("Arial",15),fill="white")
    canva.create_text(1350,100,text=f"Solde : {solde_uti} VTL",font=("Arial",15),fill="white")

# -------------------------------------------------------------------------------------------








    # Affichage de la newsletter
# -------------------------------------------------------------------------------------------

    nom,solde= nomSoldeUtiStar(indiceSoldeLePlusHaut())

    newsletter = [

                 f"Utilisateur stars : {nom}, {solde} VTL",
                  "Maintenance cette nuit de 2 h à 6 h : Site non accessible",
                  "Une nouvelle table de blackjack arrive ! Dès lundi, dans votre casino de Brissac-Quincé",                                                                    
                  "LES JEUX D'ARGENT ET DE HASARD PEUVENT ÊTRE DANGEREUX : PERTES D'ARGENT, CONFLITS FAMILIAUX, ADDICTION. RETROUVEZ NOS CONSEILS SUR : JOUEURS-INFO-SERVICE.FR (09-74-75-13-13 - APPEL NON SURTAXÉ)",
                  "Votre casino d'Angers sera exceptionnellement fermé ce soir, Pour cause : Privatisation par le fils du maire",
                  "Gagnez deux places pour : le Salon de l'agriculture En gagnant à la roulette au Casino de : Saumur",
                  "Merci à : John Deere, TaylorMade, Bricomarché de Brissac-Quincé Pour leur soutien !"
    ]
    

    canva.create_text(225,150,text="Newsletter",fill='gold',font="Rye 37")
    
    canva.create_line(30,100,420,100,width=4,fill = "gold")
    canva.create_line(30,675,420,675,width=4,fill = "gold")
    
    canva.create_line(30,100,30,675,width=4,fill = "gold")
    canva.create_line(420,100,420,675,width=4,fill = "gold")

    affichageNewsletter(newsletter)

# -------------------------------------------------------------------------------------------








    return{
        "frame": frame_menu,
        "nom": nom_uti,
        "solde_uti": solde_uti
    }

# -------------------------------------------------------------------------------------------


