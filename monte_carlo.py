from base import collect_points
import numpy as np

count_list = []

for i in range (100000):
    throw = list(np.random.randint(1, 7, 5))
    score = collect_points(throw)
    if score[0] > 0:
        count_list.append(1)
    else:
        count_list.append(0)
        
print(sum(count_list)/len(count_list))