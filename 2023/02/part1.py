COLORS = [
    "red",
    "green",
    "blue"
]
class Colors():
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.red = red
        self.green = green
        self.blue  = blue

class GameColors(Colors):
    def __init__(self, red=0, green=0, blue=0) -> None:
        super().__init__(red, green, blue)

    def is_possible(self) -> bool:
        r, g, b = (False,False,False)
        MAX_CUBE_SET = Colors(12, 13, 14)
        if self.red <= MAX_CUBE_SET.red:
            r = True
        if self.green <= MAX_CUBE_SET.green:
            g = True
        if self.blue <= MAX_CUBE_SET.blue:
            b = True
        for flag in [r,g,b]:
            if not flag:
                return False
        return True

def get_lines() -> list:
    with open("input.txt") as f:
        return f.readlines()

def get_start_index(s: str, ss: str):
    return s.find(ss)

def get_number(s: str, ss: str):
    s = s.replace(f" {ss}", "")
    return int(s)

def has_impossible(game_hands: list):
    return game_hands.__contains__(False)

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
        for hand in sets:
            hand_colors = GameColors()
            hand = hand.split(",")
            hand = [t.strip() for t in hand]
            for color in hand:
                for col in COLORS:
                    if col in color:
                        num = get_number(color, col)
                        hand_colors.__setattr__(col, num)
            hand_poss_list.append(hand_colors.is_possible())

        if not has_impossible(hand_poss_list):
            sum_ += id_

        print(f"{id_} {hand_poss_list}")

    print(sum_)