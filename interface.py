import fltk

#--Constantes------------------
LARG = 900 #Largeur de la fenêtre
HAUT = 700 #Hauteur de la fenêtre
TAILLE = 10 #Nombre de lignes et de colonnes de la grille
TAILLE_CEL = 50 #Taille d'une cellule en pixels
X_OFFSET = 70 # décallage gauche - min 30 pour afficher les références
Y_OFFSET = 50 # décallage droite - min 30
#------------------------------


def show_grid(nb_cel, taille_cel, x_offset, y_offset):
    x, y = 10, 10 #position du coin
    for i in range(nb_cel + 1) :
        #----Affichage des lignes
        fltk.ligne(x_offset + i*taille_cel, y_offset, x_offset + i*taille_cel, y_offset + nb_cel*taille_cel, couleur = 'black')
        fltk.ligne(x_offset, y_offset + i*taille_cel, x_offset + nb_cel*taille_cel, y_offset + i*taille_cel, couleur = 'black')

def show_card(nb_couleur, taille_cel, x_offset, y_offset, largeur, hauteur):
    x, y = 10, 10 #position du coin
    for i in range(nb_couleur + 1) :
        #----Affichage des lignes
        fltk.ligne(largeur - (3*taille_cel + x_offset), y_offset + i*taille_cel, largeur - x_offset, y_offset + i*taille_cel, couleur = 'black')
        if i < 4 :
            fltk.ligne(largeur - x_offset - i*taille_cel, y_offset, largeur - x_offset - i*taille_cel, y_offset + nb_couleur*taille_cel, couleur = 'black')
        

def background(LARG, HAUT, couleur):
    fltk.rectangle(0, 0, LARG, HAUT, couleur, couleur)