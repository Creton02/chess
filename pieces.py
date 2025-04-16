class Tableau():   # Le tableau s'occupera de se rappeler du positionnement de chaque pièce ainsi que des interractions entre les pièces lors des déplacements, et il s'occupera des condition de fin de parties.
    def __init__(self, liste_pieces:list):
        self.tableau = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        for Piece in liste_pieces:
            self.tableau[Piece.pos[0]][Piece.pos[1]] = Piece
    
    def deplacement(self, Piece:object, position_deplacement, tour_blanc):
        if (Piece.couleur == "blanc" and tour_blanc) or (Piece.couleur == "noir" and not tour_blanc):
            if self.tableau[position_deplacement[0]][position_deplacement[1]] != 0:
                return False
            elif (position_deplacement[0], position_deplacement[1]) in Piece.deplacement():
                self.tableau[position_deplacement[0]][position_deplacement[1]] = Piece
                self.tableau[Piece.pos[0]][Piece.pos[1]] = 0
                Piece.pos = [position_deplacement[0], position_deplacement[1]]
                return True
        
class Piece(): #Les pièces s'occuperons de dire vers quelles cases elle peuvent aller
    def __init__(self, x, y, equipe:int = 0):
        self.pos = x, y
        if equipe == 0:
            self.couleur = "noir"
        else:
            self.couleur = "blanc"
            
    def deplacement(self):
        pass

class Pion(Piece): 
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        if self.couleur == "noir":
            deplacement_pion = +1
        if self.couleur == "blanc":
            deplacement_pion = -1
        can_go.append((self.pos[0] + deplacement_pion, self.pos[1] - 1))
        can_go.append((self.pos[0] + deplacement_pion, self.pos[1]))
        can_go.append((self.pos[0] + deplacement_pion, self.pos[1] + 1))
        
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau


class Tour(Piece):
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        for i in range(1, 8):
            #Position verticales et horizontales
            can_go.append((self.pos[0] + i, self.pos[1]))
            can_go.append((self.pos[0] - i, self.pos[1]))
            can_go.append((self.pos[0], self.pos[1] + i))
            can_go.append((self.pos[0], self.pos[1] - i))
        
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau
    
class Cavalier(Piece):
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        can_go.append((self.pos[0] + 2, self.pos[1] + 1))
        can_go.append((self.pos[0] + 2, self.pos[1] - 1))
        can_go.append((self.pos[0] - 2, self.pos[1] + 1))
        can_go.append((self.pos[0] - 2, self.pos[1] - 1))
        can_go.append((self.pos[0] + 1, self.pos[1] + 2))
        can_go.append((self.pos[0] + 1, self.pos[1] - 2))
        can_go.append((self.pos[0] - 1, self.pos[1] + 2))
        can_go.append((self.pos[0] - 1, self.pos[1] - 2))
        
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau
    
class Reine(Piece):
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        for i in range(1, 8):
            #Position verticales et horizontales
            can_go.append((self.pos[0] + i, self.pos[1]))
            can_go.append((self.pos[0] - i, self.pos[1]))
            can_go.append((self.pos[0], self.pos[1] + i))
            can_go.append((self.pos[0], self.pos[1] - i))
            can_go.append((self.pos[0] + i, self.pos[1] + i))
            can_go.append((self.pos[0] + i, self.pos[1] - i))
            can_go.append((self.pos[0] - i, self.pos[1] + i))
            can_go.append((self.pos[0] - i, self.pos[1] - i))
            
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau
    
class Fou(Piece):
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        for i in range(1, 8):
            can_go.append((self.pos[0] + i, self.pos[1] + i))
            can_go.append((self.pos[0] + i, self.pos[1] - i))
            can_go.append((self.pos[0] - i, self.pos[1] + i))
            can_go.append((self.pos[0] - i, self.pos[1] - i))
            
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau
        
class Roi(Piece):
    def deplacement(self): # Retourne une liste des déplacements possible
        can_go = []
        can_go.append((self.pos[0] + 1, self.pos[1] + 1))
        can_go.append((self.pos[0] - 1, self.pos[1] + 1))
        can_go.append((self.pos[0] + 1, self.pos[1] - 1))
        can_go.append((self.pos[0] - 1, self.pos[1] - 1))
        can_go.append((self.pos[0] + 1, self.pos[1]))
        can_go.append((self.pos[0] - 1, self.pos[1]))
        can_go.append((self.pos[0], self.pos[1] + 1))
        can_go.append((self.pos[0], self.pos[1] - 1))
        
        return [(x, y) for x, y in can_go if 0 <= x < 8 and 0 <= y < 8] # Pour ne pas dépasser le tableau