

coups = [" "," "," "," "," "," "," "," "," "] 
joueur = "X"
def afficherTableau(case):
    print(" ____ ____ ____")
    print("|",coups[0], " |",coups[1], " |",coups[2], " |")
    print("|____|____|____|")
    print("|",coups[3], " |",coups[4], " |",coups[5], " |")
    print("|____|____|____|")
    print("|",coups[6], " |",coups[7], " |",coups[8], " |")
    print("|____|____|____|")



def choisirCase():
    position = (input("Choisissez une case entre 0 et 8: "))

    while position not in ["0","1","2","3","4","5","6","7","8",]:
        position = (input(" incorrecte.Choisissez une case entre 0 et 8: "))
        
    position = int(position)
    
    if coups[position] != " ":
        print("essayer une case vide")
        not changerDeJoueur()
        return False
        
    coups[position] = joueur
    afficherTableau(9)
    

def changerDeJoueur():
    global joueur 
    if joueur == "X":
        joueur = "O"
    elif joueur == "O":
        joueur = "X"
    return joueur
    
    

    
def ligneGagne():
    
    ligne1 = coups[0]==coups[1]==coups[2]=="X" or coups[0]==coups[1]==coups[2]=="O"
    ligne2 = coups[3]==coups[4]==coups[5]=="X" or coups[3]==coups[4]==coups[5]=="O"
    ligne3 = coups[6]==coups[7]==coups[8]=="X" or coups[6]==coups[7]==coups[8]=="O"
    if ligne1 or ligne2 or ligne3:
        return "X" or "O"
    

def colonneGagne():
    
    colonne1 = coups[0]==coups[3]==coups[6]=="X" or coups[0]==coups[3]==coups[6]=="o"
    colonne2 = coups[1]==coups[4]==coups[7]=="X" or coups[1]==coups[4]==coups[7]=="O"
    colonne3 = coups[2]==coups[5]==coups[8]=="X" or coups[2]==coups[5]==coups[8]=="O"
    if colonne1 or colonne2 or colonne3:
        return "X" or "O"
    

def diagonaleGagne():
    
    diagonale1 = coups[0]==coups[4]==coups[8]=="X" or coups[0]==coups[4]==coups[8]=="O"
    diagonale2 = coups[2]==coups[4]==coups[6]=="X" or coups[2]==coups[4]==coups[6]=="O"
    if diagonale1 or diagonale2:
        return "X" or "O"
    
       

def jeuTerminé():
    if conditionDeVictoire() or conditionDegalité():
        return True
    else:
        return False

def conditionDeVictoire():
    if ligneGagne() or colonneGagne() or diagonaleGagne():
        return True
    else:
        return False
    

def conditionDegalité():
    
    if " " not in coups:
        return True
    
    
def commencerLeJeu():
    print("Bienvenue au jeu du morpion")
    afficherTableau(9)
    finDePartie = jeuTerminé()
    while not finDePartie :
        print(joueur + " à toi de jouer" )
        choisirCase()
        changerDeJoueur()
        finDePartie = jeuTerminé()

    if conditionDeVictoire():
        print(changerDeJoueur(), "gagne la partie.")
        return
        
    if conditionDegalité():
        print("jeu termine : match nul")
        return  
    
    return
        
    
commencerLeJeu()