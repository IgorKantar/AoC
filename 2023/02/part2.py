from part1 import (
    get_lines,
    get_start_index,
    GameColors,
    COLORS,
    get_number,
    Colors
)

class MinPossibleColors(Colors):
    """
    Class that represents minimum required color cubes,
    for all hands in a game to be possible.
    """

    def __init__(self, red=0, green=0, blue=0) -> None:
        super().__init__(red, green, blue)

    def add_hand(self, hand: GameColors):
        for color in COLORS:
            min_col  = self.__getattribute__(color)
            hand_col = hand.__getattribute__(color)
            # if hand color value larget,
            # set as new minimum posible
            if min_col < hand_col:
                self.__setattr__(color, hand_col)

if __name__ == "__main__":
    sum_ = 0
    games = get_lines()

    for id_, game in enumerate(games):
        # failed my first submit bc i forgot this
        id_ += 1
        # forgot to give better name
        x = get_start_index(game, ":")
        # get game line without game id
        game = game[x+2:]
        # should have named this hands, get list
        # of hands in game and strip them
        sets = game.split(";")
        sets = [set_.strip() for set_ in sets]
        # 'hand possible list', list of bools that
        # will represent whether hand is possible
        hand_poss_list = []
        min_req_colors = MinPossibleColors()
        for hand in sets:
            # init hand colors
            hand_colors = GameColors()
            # make list of hand colors and strip whitespace
            hand = hand.split(",")
            hand = [t.strip() for t in hand]
            for color in hand:
                for col in COLORS:
                    # if color in hand
                    if col in color:
                        # get the int value
                        num = get_number(color, col)
                        # set color attribute, ex. equivalent
                        # to hand_colors.green = 20
                        hand_colors.__setattr__(col, num)
            min_req_colors.add_hand(hand_colors)

        power = min_req_colors.red * min_req_colors.green * min_req_colors.blue
        sum_ += power

    print(sum_)