from player import *
from game import *
from hand import *
from calculate import *

if __name__ == '__main__':
    # create some players

    some_players = [Player("Jack"), Player("Jill"), Player("Sally"), Player("Robert"), Player("Mary")]

    game = Game(some_players)

    print(game)