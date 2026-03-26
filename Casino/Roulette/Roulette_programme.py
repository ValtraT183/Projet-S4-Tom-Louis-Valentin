from random import*

selection = {"type": None, "valeur": None}    # Pour l'affichage de la sélection




ordre_roulette = [0,32, 15, 19, 4, 21, 2, 25, 17, 34,6, 27, 13, 36, 11, 30, 8, 23, 10, 5,24, 16, 33, 1, 20, 14, 31, 9, 22, 18,29, 7, 28, 12, 35, 3, 26]

def creation_dic(ordre):

    rouge =[3,12,7,18,9,14,1,16,5,23,30,36,27,34,25,21,19,32]
    
    dic = {}
    
    for i in range(len(ordre)):
        numero = ordre[i]
        
        if numero == 0:
            couleur = "Vert"
        elif numero in rouge:
            couleur = "Rouge"
        else:
            couleur = "Noir"
        
        dic[i+1] = [numero,couleur]
    
    return dic




case_numero_et_couleur = creation_dic(ordre_roulette)  #  clé : psotion sur la roue / valeur : liste avec numero et la couleur [numero,couleur]



case_coordonnees = { 1 : (900,245),
                    2 : (918,245),
                    3 : (936,245),
                    4 : (954,255),
                    5 : (968,265),
                    6 : (978,276), 
                    7 : (996,290), 
                    8 : (1000,308),
                    9 : (1005,328),
                    10 : (1005,343),
                    11 : (1005,363),
                    12 : (1005,382),
                    13 : (1000,400),
                    14 : (994,420),
                    15 : (980,432),
                    16 : (960,435),
                    17 : (948,450),
                    18 : (930,452),
                    19 : (907,458),
                    20 : (890,460), 
                    21 : (870,455),
                    22 : (855,445),
                    23 : (838,440),
                    24 : (825,428),
                    25 : (810,415),
                    26 : (805,395),
                    27 : (790,380),
                    28 : (790,365),
                    29 : (790,345),
                    30 : (790,325),
                    31 : (800,310),   
                    32 : (800,290),
                    33 : (815,275),
                    34 : (830,260),
                    35 : (848,260),
                    36 : (860,245),
                    37 : (880,245),

                    
                    

}                                                    # clé : position sur la roue / valeur : tuple coordonnées x et y (x,y)





def creation_chemin() :

    chemin = []
    debut = randint(1,37)
    i = debut
    while len(chemin) != 200 :   # environ 6 sec d'après les tests
        if i > 37 :
            i=1
        
        chemin.append(i)
        i+=1
    
    return chemin 





def recup_gain(mise,selection,case) :
    
    if selection == "Pair" and case[0] % 2 == 0 :
        return mise*2
    elif selection == "Impair" and case[0] % 2 != 0 :
        return mise*2
    elif selection == case[1] :
        return mise*2
    elif case[0] == selection :
        return mise*30
    else :
        return 0
        








        






