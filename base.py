import random as r

class Dice:
    def __init__(self, active = True):
        self.score = None
        self.active = active

    def is_active(self):
        if self.active == True:
            return True
        else:
            return False
    def throw(self):
        if self.is_active:
            self.score = r.randint(1, 6)
        else:
            self.score = None
        return self.score

    def turn_off(self):
        self.active = False

class Player:
    def __init__(self, id, risk):
        self.id = id
        self.dice = Dice()
        self.points = 0
        self.risk = risk
        self.num_of_active = 5

    def add_points(self, score):
        self.points += score

    def throw_dices(self):
        score_list = []
        for i in range(0, self.num_of_active):
            score_list.append(self.dice.throw())
        return score_list


def collect_points(throw_result):
    points = 0
    dices_thrown = len(throw_result)
    possible_scores = [1, 2, 3, 4, 5, 6]

    nums = [throw_result.count(i) for i in possible_scores]

    if 3 in nums:
        position = nums.index(3)
        if position == 0:
            points += 30
        else:
            points += 10*possible_scores[position]
        

    if 4 in nums:
        position = nums.index(4)
        if position == 0:
            points += 100
        else:
            points += 10*possible_scores[position]*possible_scores[position]
        

    if 5 in nums:
        position = nums.index(5)
        if position == 0:
            points += 1000
        else:
            points += 10*possible_scores[position]*possible_scores[position]*possible_scores[position]

    if (nums[0] == 1) or (nums[0] == 2):
        points += nums[0] * 10

    if (nums[4] == 1) or (nums[4] == 2):
        points += nums[4] * 5
        
    return points


if __name__ == "__main__":
    Bodzia = Player(1, 1)
    throw = Bodzia.throw_dices()
    print(throw)
    print(collect_points(throw))