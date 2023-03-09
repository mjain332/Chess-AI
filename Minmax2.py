# -*- coding: utf-8 -*-
"""Chess AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m0Knwv-n-jQNJ7_SFnqm31I4_yFjgtpk
"""

# importing required librarys
import pygame
import chess
import math
import os
import time
from copy import deepcopy
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

#connecting google drive
'''from google.colab import drive
drive.mount('/content/drive/')
import os
os.chdir('/content/drive/My Drive/Chess')
'''
#load piece images
pieces = {'p': pygame.image.load('pb.jpg').convert(),
          'n': pygame.image.load('nb.png').convert(),
          'b': pygame.image.load('bb.png').convert(),
          'r': pygame.image.load('rb.png').convert(),
          'q': pygame.image.load('qb.png').convert(),
          'k': pygame.image.load('kd.png').convert(),
          'P': pygame.image.load('pw.png').convert(),
          'N': pygame.image.load('nw.png').convert(),
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

scoring= {'p': -1,
          'n': -3,
          'b': -3,
          'r': -5,
          'q': -9,
          'k': 0,
          'P': 1,
          'N': 3,
          'B': 3,
          'R': 5,
          'Q': 9,
          'K': 0,
          }
#simple evaluation function
def eval_board(BOARD):
    score = 0
    pieces = BOARD.piece_map()
    for key in pieces:
        score += scoring[str(pieces[key])]

    return score
#this is min_max at depth one
def most_value_agent(BOARD):

    moves = list(BOARD.legal_moves)
    scores = []
    for move in moves:
        #creates a copy of BOARD so we dont
        #change the original class
        temp = deepcopy(BOARD)
        temp.push(move)

        scores.append(eval_board(temp))

    if BOARD.turn == True:
        best_move = moves[scores.index(max(scores))]

    else:
        best_move = moves[scores.index(min(scores))]

    return best_move
def min_max2(BOARD):
    moves = list(BOARD.legal_moves)
    scores = []

    for move in moves:
        temp = deepcopy(BOARD)
        temp.push(move)
        temp_best_move = most_value_agent(temp)
        temp.push(temp_best_move)
        scores.append(eval_board(temp))

    if BOARD.turn == True:
        
        best_move = moves[scores.index(max(scores))]

    else:
        best_move = moves[scores.index(min(scores))]

    return best_move

def main(BOARD,agent1,agent_color1,agent2):
    
    #make background black
    scrn.fill(YELLOW)
    #name window
    pygame.display.set_caption('Chess')

    status = True
    while (status):
        #update screen
        update(scrn,BOARD)
        time.sleep(.5)
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
  main(b,random_agent,True,min_max2)

