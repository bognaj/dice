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



if __name__ == "__main__":
    Bodzia = Player(1, 1)
    print(Bodzia.throw_dices())