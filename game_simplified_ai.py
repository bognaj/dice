import pygame, sys,os
from pygame.locals import *
import os.path
import random
import time
from base import collect_points
from base import Dice

pygame.init()

# screen size
SCREEN_WIDTH=400
SCREEN_HEIGHT=600
SCREEN_SIZE=(SCREEN_WIDTH, SCREEN_HEIGHT)

# colors
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
BLUE2 = (0, 100, 255)

font = pygame.font.SysFont('arial', 25)

class DiceGameAI:
    def __init__(self): # initiating the game
        self.display = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("Dice game for AI")
        self.clock = pygame.time.Clock()
        
        self.dice = Dice()    
        self.active = 5 # num of active dices
        self.overall_points = 0 # points in whole game
        self.this_round_points = 0 # points in this turn
        self.rounds = 0 # num of rounds needed to achieve 1000
        
        
    def reset(self):
        # init game state
        self.active = 5
        self.overall_points = 0
        self.this_round_points = 0
        self.rounds = 0

        self.frame_iteration = 0    
        
    def throw_dices(self, num_of_active):
        # throwing all active dices
        score_list = []
        for i in range(0, num_of_active):
            score_list.append(self.dice.throw())
        return score_list
        
    def play_step(self, action):
        game_over = False
        reward = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if action[0] == 0:
            return self.keep_rolling()
        elif action[0] == 1:
            return self.save_score()
                
        self._update_ui()
        
        return reward, game_over, self.rounds
        
    def keep_rolling(self):
        # decision to throw the dices
        throw = self.throw_dices(self.active)
        points = collect_points(throw)
        
        # failure
        if points[0] == 0:
            self.active = 5
            self.this_round_points = 0
            game_over = False
            self.rounds += 1
            reward = -1
            
        else:
            self.this_round_points += points[0]
            dice_num = self.active - points[1]
            reward = 1
            
            if dice_num == 0:
                self.active = 5
            else:
                self.active = dice_num    
            game_over = False    
        return reward, game_over, self.rounds
        
        
    def save_score(self):
        # saving the score instead of further throwing
        if self.this_round_points == 0:
            game_over = False
            self.rounds += 1
            reward = -5
            
        else:
            self.overall_points += self.this_round_points
            if self.overall_points >= 1000:
                reward = 100
                game_over = True
            else:
                reward = 5
                game_over = False
            self.this_round_points = 0
            self.active = 5
            self.rounds += 1
        return reward, game_over, self.rounds
                      
    def _update_ui(self):
        # displaying all the game elements
        self.display.fill(BLACK)
        
        self.button_throw = pygame.draw.rect(self.display, BLUE2, (25, 200, 200, 70), 0)
        self.display.blit(font.render('Rzucaj', True, (255, 255, 255)),(50, 225))
        
        self.button_save = pygame.draw.rect(self.display, BLUE2, (25, 300, 200, 70), 0)
        self.display.blit(font.render('Zapisz', True, (255, 255, 255)), (50, 325))
        
        text = font.render("Score: " + str(self.overall_points), True, WHITE)
        self.display.blit(text, [0, 0])
        
        text1 = font.render("Score: " + str(self.this_round_points), True, WHITE)
        self.display.blit(text1, [100, 100])
        
        text2 = font.render("Rounds: " + str(self.rounds), True, WHITE)
        self.display.blit(text2, [200, 0])
        
        text3 = font.render("Dices: " + str(self.active), True, WHITE)
        self.display.blit(text3, [100, 150])
        
        pygame.display.flip()
