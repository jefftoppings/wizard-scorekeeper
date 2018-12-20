class Game(object):

    def __init__(self, players_list):
        self.players = players_list

    def __str__(self):
        for player in self.players:
            print(player.name + ":", player.score)

