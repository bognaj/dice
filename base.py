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
        throw = self.throw_dices(5)
        print(throw)
        res = collect_points(throw)
        self.add_points(res[0])
        act = 5 - res[1]
        while res[0] > 0:
            if act > 0:
                throw = self.throw_dices(act)
                print(throw)
                res = collect_points(throw)
                self.add_points(res[0])
                act -= res[1]
            elif act == 0:
                act = 5
                throw = self.throw_dices(act)
                print(throw)
                res = collect_points(throw)
                self.add_points(res[0])
                act -= res[1]
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


if __name__ == "__main__":
    Bodzia = Player(1, 1)
    print(Bodzia.one_turn())