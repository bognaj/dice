from itertools import count
from base import collect_points
import numpy as np

def if_any_points(k): # probability of throw with points if we have k dices
    count_list = []
    for i in range (100000):
        throw = list(np.random.randint(1, 7, k))
        score = collect_points(throw)
        if score[0] > 0:
            count_list.append(1)
        else:
            count_list.append(0)
        
    return sum(count_list)/len(count_list)

def mean_point_score(k): # mean score while throwing k dices
    count_list = []
    for i in range(100000):
        throw = list(np.random.randint(1, 7, k))
        score = collect_points(throw)
        count_list.append(score[0])
    return np.mean(np.array(count_list))

print(mean_point_score(5))        