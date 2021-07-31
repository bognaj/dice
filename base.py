import random as r

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
                if save_score(max([self.risk - change_risk(act), 0])):
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
                        if (save_score(max([self.risk - change_risk(act), 0])) and (curr >= 25)) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                else:
                    if self.points >= 900: # ending the game
                        if (curr >= 1000 - self.points) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                    else:
                        if (save_score(max([self.risk - change_risk(act), 0])) and (curr >= 25)) and (res[0] > 0):
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
                        if save_score(max([self.risk - change_risk(act), 0])):
                            self.add_points(curr)
                            res = [0, 0]
                else:
                    if self.points >= 900:
                        if (curr >= 1000 - self.points) and (res[0] > 0):
                            self.add_points(curr)
                            res = [0, 0]
                    else:
                        if (save_score(max([self.risk - change_risk(act), 0])) and (curr >= 25)) and (res[0] > 0):
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
    


if __name__ == "__main__":
    Roman = Player(1, 0.7)
    Lidia = Player(2, 0.3)
    Bodzia = Player(3, 0.5)
    Milosz = Player(4, 0.2)
    print("R|" + "           " + "L|" + "           " + "B|" + "           " + "M")
    print("----------------------------------------------------------------------------------")
    while ((Bodzia.points < 1000) and (Milosz.points < 1000)) and ((Lidia.points < 1000) and (Roman.points < 1000)):
        Roman.one_turn()
        Lidia.one_turn()
        Bodzia.one_turn()
        Milosz.one_turn()
        print(str(Roman.points) + "|           " + str(Lidia.points) + "|          " + str(Bodzia.points) + "|          " + str(Milosz.points))
    