COLORS = [
    "red",
    "green",
    "blue"
]
class Colors():
    """Class representing colors used in the game."""
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.red = red
        self.green = green
        self.blue  = blue

class GameColors(Colors):
    def __init__(self, red=0, green=0, blue=0) -> None:
        super().__init__(red, green, blue)

    def is_possible(self) -> bool:
        # flag tuple
        r, g, b = (False,False,False)
        # color class repring max number of cubes
        MAX_CUBE_SET = Colors(12, 13, 14)
        if self.red <= MAX_CUBE_SET.red:
            r = True
        if self.green <= MAX_CUBE_SET.green:
            g = True
        if self.blue <= MAX_CUBE_SET.blue:
            b = True
        # return False if any cube colors are over max allowed
        for flag in [r,g,b]:
            if not flag:
                return False
        return True

def get_lines() -> list:
    # return list of lines
    with open("input.txt") as f:
        return f.readlines()

def get_start_index(s: str, ss: str):
    # return starting index of substring
    return s.find(ss)

def get_number(s: str, ss: str):
    # return integer value of hand color
    # ex. "8 green" -> "8" -> 8
    s = s.replace(f" {ss}", "")
    return int(s)

def has_impossible(game_hands: list):
    # game_hands is list of bools
    # return True if game contains impossible hand
    return game_hands.__contains__(False)

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
            # append hand possible flag
            hand_poss_list.append(hand_colors.is_possible())

        # if all flags True, add id to sum
        if not has_impossible(hand_poss_list):
            sum_ += id_

        print(f"{id_} {hand_poss_list}")

    print(sum_)