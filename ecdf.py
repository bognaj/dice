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

def show_plot():
    x = np.sort(res_arr)
    y = np.arange(len(x))/float(len(x))
    plt.plot(x, y)
    plt.show()

def show_probability():
    p0 = np.sum(np.where(res_arr <= 0, 1, 0))
    print(p0/len(res_arr), 0)

    p5 = np.sum(np.where(res_arr <= 5, 1, 0))
    print(p5/len(res_arr), 5)
    
    p10 = np.sum(np.where(res_arr <= 10, 1, 0))
    print(p10/len(res_arr), 10)

    p15 = np.sum(np.where(res_arr <= 15, 1, 0))
    print(p15/len(res_arr), 15)

    p20 = np.sum(np.where(res_arr <= 20, 1, 0))
    print(p20/len(res_arr), 20)

    p25 = np.sum(np.where(res_arr <= 25, 1, 0))
    print(p25/len(res_arr), 25)

    p30 = np.sum(np.where(res_arr <= 30, 1, 0))
    print(p30/len(res_arr), 30)

    p35 = np.sum(np.where(res_arr <= 35, 1, 0))
    print(p35/len(res_arr), 35)
    
    p40 = np.sum(np.where(res_arr <= 40, 1, 0))
    print(p40/len(res_arr), 40)

    p45 = np.sum(np.where(res_arr <= 45, 1, 0))
    print(p45/len(res_arr), 45)

    p50 = np.sum(np.where(res_arr <= 50, 1, 0))
    print(p50/len(res_arr), 50)

    p55 = np.sum(np.where(res_arr <= 55, 1, 0))
    print(p55/len(res_arr), 55)

    p60 = np.sum(np.where(res_arr <= 60, 1, 0))
    print(p60/len(res_arr), 60)

    p65 = np.sum(np.where(res_arr <= 65, 1, 0))
    print(p65/len(res_arr), 65)
    
    p70 = np.sum(np.where(res_arr <= 70, 1, 0))
    print(p70/len(res_arr), 70)

    p75 = np.sum(np.where(res_arr <= 75, 1, 0))
    print(p75/len(res_arr), 75)

    p80 = np.sum(np.where(res_arr <= 80, 1, 0))
    print(p80/len(res_arr), 80)

    p85 = np.sum(np.where(res_arr <= 85, 1, 0))
    print(p85/len(res_arr), 85)

    p90 = np.sum(np.where(res_arr <= 90, 1, 0))
    print(p90/len(res_arr), 90)

def calculate_stats():    
    EX = np.mean(res_arr)
    VarX = np.var(res_arr)
    print(EX)
    print(VarX)

def save_data():    
    a_file = open("results.txt", "w")
    np.savetxt(a_file, res_arr)
