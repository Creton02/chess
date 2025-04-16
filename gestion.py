import pygame
import sys
from pieces import Pion, Tour, Tableau, Cavalier, Reine, Roi, Fou
pygame.init()

#Constantes
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BRUN = (144, 155, 155)
SURLIGNAGE = (155, 255, 155)
SURLIGNAGE2 = (255, 155, 155)
SURLIGNAGE3 = (155, 155, 255)

#Écran
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Chess")

#Préparation du tableau de jeu
liste_pieces = []

#Initialisation équipe noir
for e in range(8):
    liste_pieces.append(Pion(1, e))
liste_pieces.append(Cavalier(0, 1))
liste_pieces.append(Cavalier(0, 6))
liste_pieces.append(Tour(0, 0))
liste_pieces.append(Tour(0, 7))
liste_pieces.append(Reine(0, 3))
liste_pieces.append(Roi(0, 4))
liste_pieces.append(Fou(0, 2))
liste_pieces.append(Fou(0, 5))

#Initialisation équipe blanc
for e in range(8):
    liste_pieces.append(Pion(6, e, equipe=1))
liste_pieces.append(Cavalier(7, 1, equipe=1))
liste_pieces.append(Cavalier(7, 6, equipe=1))
liste_pieces.append(Tour(7, 0, equipe=1))
liste_pieces.append(Tour(7, 7, equipe=1))
liste_pieces.append(Reine(7, 3, equipe=1))
liste_pieces.append(Roi(7, 4, equipe=1))
liste_pieces.append(Fou(7, 2, equipe=1))
liste_pieces.append(Fou(7, 5, equipe=1))

#Initialisation du tableau
board = Tableau(liste_pieces)

selected_square = None
second_selected_square = None
tour_blanc = True

def draw_board(win):
    for row in range(ROWS):
        for col in range(COLS):
            
            color = BLANC if (row + col) % 2 == 0 else NOIR
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(win, color, rect)
            
            if board.tableau[row][col] != 0:
                pygame.draw.rect(win, BRUN, rect)
            
            # Highlight selected square
            if selected_square == (row, col):
                pygame.draw.rect(win, SURLIGNAGE, rect, 4)
            """if second_selected_square == (row, col):
                pygame.draw.rect(win, SURLIGNAGE2, rect, 4)"""
            
    if selected_square: # Highlight possible moves
        piece = board.tableau[selected_square[0]][selected_square[1]]
        if piece != 0:
            if (piece.couleur == "blanc" and tour_blanc) or (piece.couleur == "noir" and not tour_blanc):
                for move in piece.deplacement():
                    row, col = move
                    if 0 <= row < 8 and 0 <= col < 8:
                        highlight_rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                        pygame.draw.rect(win, SURLIGNAGE3, highlight_rect, 3)
            

def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    if 0 <= row < 8 and 0 <= col < 8:
        return (row, col)
    return None

running = True
while running:
    draw_board(WIN)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clicked_square = get_square_under_mouse(pygame.mouse.get_pos())
            if clicked_square:
                if selected_square == clicked_square:
                    selected_square = None  # Déselectionner
                elif selected_square != None and second_selected_square == None:
                    second_selected_square = clicked_square # Sélectionner un second carré
                    if board.tableau[selected_square[0]][selected_square[1]] != 0:  
                        deplacement_fait = board.deplacement(board.tableau[selected_square[0]][selected_square[1]], clicked_square, tour_blanc)
                        if deplacement_fait == True:
                            selected_square = None
                            second_selected_square = None
                            tour_blanc = not tour_blanc
                elif selected_square != None and second_selected_square != None:
                    selected_square = clicked_square # Désectionner le second carré et sélectionner le nouveau carré
                    second_selected_square = None
                else:
                    selected_square = clicked_square # Sélectionner le nouveau carré
pygame.quit()
sys.exit()    

  
def main():
    pass


if __name__ == "__main__":
    main()