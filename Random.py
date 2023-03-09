import pygame
import chess
import math
#creating dummy display
import os
os.environ['SDL_VIDEODRIVER']='dummy'
#initialise display
X = 800
Y = 800
scrn = pygame.display.set_mode((X, Y))
pygame.init()
#basic colours
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (0, 0, 0)
#initialise chess board
b = chess.Board()
#load piece images
pieces = {'p': pygame.image.load('pb.png').convert(),
          'n': pygame.image.load('nb.png').convert(),
          'b': pygame.image.load('bb.png').convert(),
          'r': pygame.image.load('rb.png').convert(),
          'q': pygame.image.load('qb.png').convert(),
          'k': pygame.image.load('kd.png').convert(),
          'P': pygame.image.load('pw.png').convert(),
          'N': pygame.image.load('kw.png').convert(),
          'B': pygame.image.load('bw.png').convert(),
          'R': pygame.image.load('rw.png').convert(),
          'Q': pygame.image.load('qw.png').convert(),
          'K': pygame.image.load('kw.png').convert(),
          
          }
def update(scrn,board): # updates the screen basis the board class
    
    for i in range(64):
        piece = board.piece_at(i)
        if piece == None:
            pass
        else:
            scrn.blit(pieces[str(piece)],((i%8)*100,700-(i//8)*100))
    
    for i in range(7):
        i=i+1
        pygame.draw.line(scrn,WHITE,(0,i*100),(800,i*100))
        pygame.draw.line(scrn,WHITE,(i*100,0),(i*100,800))

    pygame.display.flip()
import random
def random_agent(BOARD):
    return random.choice(list(BOARD.legal_moves))
def main(BOARD,agent1,agent_color1,agent2):
    
    #make background black
    scrn.fill(BLACK)
    #name window
    pygame.display.set_caption('Chess')

    status = True
    while (status):
        #update screen
        update(scrn,BOARD)
        
        if BOARD.turn==agent_color1:
            BOARD.push(agent1(BOARD))

        else:
            BOARD.push(agent2(BOARD))

        scrn.fill(BLACK)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status = False
     
    # deactivates the pygame library
        if BOARD.outcome() != None:
            print(BOARD.outcome())
            status = False
            print(BOARD)
    pygame.quit()

if __name__=="__main__":
  main(b,random_agent,True,random_agent)
