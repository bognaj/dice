from base import Player
from base import Dice
from base import collect_points
import matplotlib.pyplot as plt
import numpy as np

player = Player(1, 0)

results = []

for i in range(1000000):
    results.append(player.till_the_end())
    
res_arr = np.array(results)

def show_plot(): # ecdf plot
    x = np.sort(res_arr)
    y = np.arange(len(x))/float(len(x))
    plt.plot(x, y)
    plt.show()

def show_probability(k): # probability of score <= k
    pk = np.sum(np.where(res_arr <= k, 1, 0))
    print(pk/len(res_arr), 0)

def calculate_stats():  # mean and variance
    EX = np.mean(res_arr)
    VarX = np.var(res_arr)
    print(EX)
    print(VarX)

def save_data(): # save data to file
    a_file = open("results.txt", "w")
    np.savetxt(a_file, res_arr)
