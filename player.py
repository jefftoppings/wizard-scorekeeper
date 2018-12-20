class Player(object):

    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, score):
        self.score += score

