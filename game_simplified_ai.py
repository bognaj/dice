from base import collect_points
from base import Dice

class DiceGameAI:
    def __init__(self): # initiating the game
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
        if action[0] == 0:
            return self.keep_rolling()
        elif action[0] == 1:
            return self.save_score()
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
            reward = -5
            
        else:
            self.this_round_points += points[0]
            dice_num = self.active - points[1]
            reward = 5
            
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
            reward = -10
            
        else:
            self.overall_points += self.this_round_points
            if self.overall_points >= 1000:
                reward = 100
                game_over = True
            else:
                reward = 1
                game_over = False
            self.this_round_points = 0
            self.active = 5
            self.rounds += 1
        return reward, game_over, self.rounds
                    



