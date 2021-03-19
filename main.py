import pygame
import os
import random

pygame.init()
pygame.font.init()

# Constant Variables
DIMENSIONS = (380,410)
SCREEN = pygame.display.set_mode(DIMENSIONS)
TITLE = pygame.display.set_caption("Color Tac")
FPS = 60
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREEN = (106,177,135)
BLUE = (0,145,213)
GREY = (100, 100, 100)
WINNER_FONT = pygame.font.SysFont('comicsans', 60)

# Players
player = [GREEN, BLUE]
player_win = ['GREEN WON!', 'BLUE WON!']
n = random.randint(0, 1)
turn = player[n]
is_winner = False
is_tie = False

# Squares
SQUARE_WIDTH, SQUARE_HEIGHT = 100, 100

lst_squares = [pygame.Rect(20,50, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(140,50, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(260,50, SQUARE_WIDTH, SQUARE_HEIGHT),
               
               pygame.Rect(20,170, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(140,170, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(260,170, SQUARE_WIDTH, SQUARE_HEIGHT),
               
               pygame.Rect(20,290, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(140,290, SQUARE_WIDTH, SQUARE_HEIGHT),
               pygame.Rect(260,290, SQUARE_WIDTH, SQUARE_HEIGHT),
               ]

square_color = []

def draw_board():
    global square_color
    square_color = []
    
    SCREEN.fill(WHITE)
    
    for square in range(9):
        pygame.draw.rect(SCREEN, BLACK, lst_squares[square])
        square_color.append(BLACK)
    
    pygame.display.update()


# Check the board if there's a winner
def check_board():
    global is_winner, is_tie
    
    def check_all():
        if is_winner == False:
            for i in range(9):
                if square_color[i] != BLACK:
                    continue
                else:
                    return False
                
            return True

        return False
            
    
    def check_horizontally(i):
        global is_winner
        try:
            if i == 0 or i == 3 or i == 6:
                if square_color[i] == square_color[i+1] and square_color[i] == square_color[i+2] and square_color[i] != BLACK:
                    is_winner = True
        except:
            pass
        
    def check_vertically(i):
        global is_winner
        try:
            if i == 0 or i == 1 or i == 2:
                if square_color[i] == square_color[i+3] and square_color[i] == square_color[i+6] and square_color[i] != BLACK:
                    is_winner = True
        except:
            pass
    
    def check_diagonally(i):   
        global is_winner
        
        try:
            if square_color[i] == square_color[i+4] and square_color[i] == square_color[i+8] and square_color[i] != BLACK:
                is_winner = True
            
            if i == 2:
                if square_color[i] == square_color[i+2] and square_color[i] == square_color[i+4] and square_color[i] != BLACK:
                    is_winner = True
                
        except:
            pass
    
    for index in range(9):
        check_vertically(index)
        check_horizontally(index)
        check_diagonally(index)
    
    if check_all() == True and is_winner == False:
        is_tie = True
        
        
# When clicked, the color changes
def change_color(index):
    global turn
        
    if square_color[index] == BLACK:
        pygame.draw.rect(SCREEN, turn, lst_squares[index])
        
        square_color.pop(index)
        square_color.insert(index, turn)
        
        if turn == BLUE:
            turn = GREEN
        else:
            turn = BLUE
        
    pygame.display.update()
    
# Draw the winner
def draw_winner(winner):
    draw_winner = WINNER_FONT.render(winner, 1, GREY)
    SCREEN.blit(draw_winner, (DIMENSIONS[0]/2 - draw_winner.get_width()/2, 5))

def draw_turn(turn):
    draw_turn = WINNER_FONT.render(turn, 1, GREY)
    SCREEN.blit(draw_turn, (DIMENSIONS[0]/2 - draw_turn.get_width()/2, 5))
    pygame.display.update()

# Main Function
def main():
    """Main function of the game"""
    global is_winner, is_tie
    
    draw_board()
    
    run_status = True
    while run_status:
        pygame.time.Clock().tick(FPS)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_status = False
                pygame.quit()
        
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos_mouse = pygame.mouse.get_pos()
                for index, square in enumerate(lst_squares):
                    if square.collidepoint(pos_mouse):
                        change_color(index)  
                        check_board()
                        
                        if is_tie == True and is_winner == False:
                            draw_winner("TIE")
                            pygame.display.update()
                            pygame.time.delay(1000)
                            is_tie = False
                            main()
                            
                        if is_winner == True:
                            winner = player.index(turn) - 1
                            draw_winner(player_win[winner])
                            pygame.display.update()
                            pygame.time.delay(1000)
                            is_winner = False
                            main()
        
        
if __name__ == '__main__':
    main()
    