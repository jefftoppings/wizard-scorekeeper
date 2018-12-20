from hand import *
from calculate import *


class Game(object):

    def __init__(self, players_list):
        self.players = players_list
        self.number_of_hands = 60 // len(players_list)
        self.current_hand = 1

    def __str__(self):
        # string = "Hand " + str(self.current_hand) + " of " + str(self.number_of_hands) + '\n\n'
        string = ''
        for player in self.players:
            string += player.name + ": " + str(player.score) + '\n'
        return string

    def new_hand(self, bets):
        """
        Record the bets for a new hand
        :param bets: list containing bets of players in proper ordering of seating
        :return: list of bets represented as Hand objects
        """
        hands = []

        for i in range(len(self.players)):
            hands.append(Hand(self.players[i], bets[i]))

        return hands

    def update_scores(self, hands, correct):
        """
        Updates the players scores based on their bets and if they are correct/incorrect
        :param hands: list of hand objects
        :param correct: list containing how many bet was off by
        :return: None
        """

        for i in range(len(hands)):
            if correct[i] == 0:
                Calculate.correct(hands[i])
            else:
                Calculate.incorrect(hands[i], correct[i])

        self.current_hand += 1

