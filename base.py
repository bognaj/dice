import random as r

class Dice:
    def __init__(self, id):
        self.id = id
        self.score = None
    def throw(self):
        self.score = r.randint(1, 6)

if __name__ == "__main__":
    pass