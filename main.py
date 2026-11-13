import fltk

#--Constantes------------------
LARG = 800 #Largeur de la fenêtre
HAUT = 600 #Hauteur de la fenêtre
TAILLE = 8 #Nombre de lignes et de colonnes de la grille
TAILLE_CEL = 50 #Taille d'une cellule en pixels
X_OFFSET = 100 # décallage gauche - min 30 pour afficher les références
Y_OFFSET = 50 # décallage droite - min 30
#------------------------------


def show_grid(nb_cel, taille_cel, x_offset, y_offset):
    """
    Affiche une grille carrée.
    
    :param nb_cel: (int) nombre de colonnes et nombre de cellules par ligne
    :param taille_cel: (int) taille d'une cellule en pixels
    :param x_offset: (int) décalage, en pixels, par rapport au bord gauche de la fenêtre
    :param y_offset: (int) décalage, en pixels, par rapport au bord supérieur de la fenêtre
    
    :return: None
    """
    x, y = 10, 10 #position du coin
    for i in range(nb_cel + 1) :
        #----Affichage des lignes
        fltk.ligne(x_offset + i*taille_cel, y_offset, x_offset + i*taille_cel, y_offset + nb_cel*taille_cel, couleur = 'gray')
        fltk.ligne(x_offset, y_offset + i*taille_cel, x_offset + nb_cel*taille_cel, y_offset + i*taille_cel, couleur = 'gray')



#---Programme principal--------------
if __name__ == "__main__":

    fltk.cree_fenetre(LARG, HAUT)
    #fltk.repere(50) # Affichage d'un repère

    show_grid(TAILLE, TAILLE_CEL, X_OFFSET, Y_OFFSET)
    
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "Quitte":
            break
        fltk.mise_a_jour()
    
    fltk.attend_fermeture()
    