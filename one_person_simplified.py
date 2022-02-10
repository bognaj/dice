from base import Player
from base import Dice
from base import collect_points
import matplotlib.pyplot as plt
import numpy as np


    
def game(limits):
    player = Player(1, 0, limits)
    results = []
    
    while player.points < 1000:
        x = player.simple_one_turn()
        results.append(x)
        
    return len(results)
        
        
def series(limits):
    length = []
    
    for i in range(100):
        y = game(limits)
        length.append(y)
        
    return np.mean(np.array(length))


            