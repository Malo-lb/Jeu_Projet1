import fltk
from interface import *


#---Programme principal--------------
if __name__ == "__main__":

    fltk.cree_fenetre(LARG, HAUT)
    #fltk.repere(50) # Affichage d'un repère

    background(LARG, HAUT, "green")
    show_grid(TAILLE, TAILLE_CEL, X_OFFSET, Y_OFFSET)
    show_card(TAILLE, TAILLE_CEL, X_OFFSET, Y_OFFSET, LARG, HAUT)
    
    while True:
        ev = fltk.attend_ev()
        typeEv = fltk.type_ev(ev)
        if typeEv == "Quitte":
            break
        fltk.mise_a_jour()
    
    fltk.attend_fermeture()
    