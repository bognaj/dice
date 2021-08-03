import random as r
import statistics as st
import matplotlib.pyplot as plt
import numpy as np

class Dice:
    """Class representing dice"""
    def __init__(self, active = True):
        self.score = None
        self.active = active

    def is_active(self):
        """Check if you can throw the dice"""
        if self.active:
            return True
        else:
            return False

    def throw(self):
        """Throwing symmetric dice"""
        if self.is_active:
            self.score = r.randint(1, 6)
        else:
            self.score = None
        return self.score

    def turn_off(self):
        """Block using the dice"""
        self.active = False

class Player:
    """Class representing player"""
    def __init__(self, id, risk):
        # player id
        self.id = id
        # player's dice
        self.dice = Dice()
        # initial points level
        self.points = 0
        # eagerness to take the risk
        self.risk = risk

    def add_points(self, score):
        """"Update player's points"""
        self.points += score

    def throw_dices(self, num_of_active):
        """Throw results"""
        score_list = []
        for i in range(0, num_of_active):
            score_list.append(self.dice.throw())
        return score_list

    def one_turn(self):
        """One player's turn"""
        curr = 0
        throw = self.throw_dices(5)
        res = collect_points(throw)
        curr += res[0]
        act = 5 - res[1]
        if self.points == 0:
            if curr >= 75: # entering the game
                if save_score(min([self.risk + change_risk(act), 1])):
                    self.add_points(curr)
                    res = [0, 0]
        while res[0] > 0:
            if act > 0:
                throw = self.throw_dices(act)
                res = collect_points(throw)
                curr += res[0]
                act -= res[1]
                if self.points == 0:
                    if curr >= 75:
                        if (save_score(min([self.risk + change_risk(act), 1])) and (curr >= 25)) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                else:
                    if self.points >= 900: # ending the game
                        if (curr >= 1000 - self.points) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                    else:
                        if (min([self.risk + change_risk(act), 1])) and (curr >= 25) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
            elif act == 0:
                act = 5
                throw = self.throw_dices(act)
                res = collect_points(throw)
                curr += res[0]
                act -= res[1]
                if self.points == 0:
                    if (curr >= 75) and (res[0] > 0):
                        if save_score(min([self.risk + change_risk(act), 1])):
                            self.add_points(curr)
                            res = [0, 0]
                else:
                    if self.points >= 900:
                        if (curr >= 1000 - self.points) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                    else:
                        if (save_score(min([self.risk + change_risk(act), 1])) and (curr >= 25)) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
        return self.points


def collect_points(throw_result):
    """Calculating the throw score"""
    points = 0
    pointed_dices = 0
    possible_scores = [1, 2, 3, 4, 5, 6]

    # counting occurances of each value in one throw
    nums = [throw_result.count(i) for i in possible_scores]

    # finding triple and more values
    if 3 in nums:
        position = nums.index(3)
        if position == 0:
            points += 30
        else:
            points += 10*possible_scores[position]
        pointed_dices += 3
        
    if 4 in nums:
        position = nums.index(4)
        if position == 0:
            points += 100
        else:
            points += 10*possible_scores[position]*possible_scores[position]
        pointed_dices += 4
    
    # finding ones and fives
    if 5 in nums:
        position = nums.index(5)
        if position == 0:
            points += 1000
        else:
            points += 10*possible_scores[position]*possible_scores[position]*possible_scores[position]
        pointed_dices += 5

    if (nums[0] == 1) or (nums[0] == 2):
        points += nums[0] * 10
        pointed_dices += nums[0]

    if (nums[4] == 1) or (nums[4] == 2):
        points += nums[4] * 5
        pointed_dices += nums[4]
        
    return (points, pointed_dices)

def save_score(risk):
    # decision whether to save the score or risk and go ahead
    var = r.random()
    if var > risk:
        return True
    else:
        return False

def change_risk(dice_num):
    if (dice_num == 0) or (dice_num == 5):
        return 0.2
    elif dice_num == 1:
        return 0
    elif dice_num == 2:
        return 0.05
    elif dice_num == 3:
        return 0.1
    elif dice_num == 4:
        return 0.15

def simulation():
    risks = np.arange(0, 1, 0.05)
    scores = [[] for i in range(0, len(risks))]

    for i in range(1000):
        id = 1
        players = []
        for i in risks:
            pl = Player(id, i)
            players.append(pl)
            id += 1

        points = [[] for i in players]

        while all( i.points < 1000 for i in players):
            for j in players:
                j.one_turn()
                ind = players.index(j)
                points[ind].append(j.points)

        for i in range(0, len(points)):
            scores[i].append(points[i][-1])
    
    wins = []
    means = []
    medians = []
    stdevs = []
    for i in range(len(scores)):
        pl_wins = sum([j >= 1000 for j in scores[i]])
        pl_mean = st.mean(scores[i])
        pl_median = st.median(scores[i])
        pl_stdev = st.stdev(scores[i])
        wins.append(pl_wins)
        means.append(pl_mean)
        medians.append(pl_median)
        stdevs.append(pl_stdev)

    plt.subplot(2, 2, 1)
    plt.scatter(risks, wins)
    plt.xlabel("risk")
    plt.ylabel("number of wins")
    plt.title("WINS")

    plt.subplot(2, 2, 2)
    plt.scatter(risks, means)
    plt.xlabel("risk")
    plt.ylabel("mean score")
    plt.title("MEAN")

    plt.subplot(2, 2, 3)
    plt.scatter(risks, medians)
    plt.xlabel("risk")
    plt.ylabel("median")
    plt.title("MEDIAN")

    plt.subplot(2, 2, 4)
    plt.scatter(risks, stdevs)
    plt.xlabel("risk")
    plt.ylabel("standard deviation")
    plt.title("STANDARD DEVIATION")

    plt.show()

    
        

if __name__ == "__main__":
    simulation()





