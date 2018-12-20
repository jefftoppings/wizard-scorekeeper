
class Calculate(object):

    @staticmethod
    def correct(hand):
        hand.player.add_score(20 + hand.bet*10)

    @staticmethod
    def incorrect(hand, off_by):
        hand.player.add_score(-10*off_by)


