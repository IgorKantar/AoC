from part1 import (
    get_lines,
    get_start_index,
    GameColors,
    COLORS,
    get_number,
    Colors
)

class MinPossibleColors(Colors):
    def __init__(self, red=0, green=0, blue=0) -> None:
        super().__init__(red, green, blue)

    def add_hand(self, hand: GameColors):
        for color in COLORS:
            min_col  = self.__getattribute__(color)
            hand_col = hand.__getattribute__(color)
            if min_col < hand_col:
                self.__setattr__(color, hand_col)

if __name__ == "__main__":
    sum_ = 0
    games = get_lines()

    for id_, game in enumerate(games):
        id_ += 1
        x = get_start_index(game, ":")
        game = game[x+2:]
        sets = game.split(";")
        sets = [set_.strip() for set_ in sets]
        hand_poss_list = []
        min_req_colors = MinPossibleColors()
        for hand in sets:
            hand_colors = GameColors()
            hand = hand.split(",")
            hand = [t.strip() for t in hand]
            for color in hand:
                for col in COLORS:
                    if col in color:
                        num = get_number(color, col)
                        hand_colors.__setattr__(col, num)
            min_req_colors.add_hand(hand_colors)

        power = min_req_colors.red * min_req_colors.green * min_req_colors.blue
        sum_ += power

    print(sum_)