class Game(object):

    def __init__(self, players_list):
        self.players = players_list
        self.number_of_hands = 60 // len(players_list)

    def __str__(self):
        for player in self.players:
            print(player.name + ":", player.score)

