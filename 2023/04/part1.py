import re

class Card():
    def __init__(self, winning:list[int], have:list[int]) -> None:
        # list winning numbers of cards
        self.winning = winning
        # number list
        self.having  = have
        # numbers in both lists, have and is winning number
        self.have_win = self.get_winning()

    def get_winning(self) -> list:
        winning = []
        for n in self.having:
            if n in self.winning:
                winning.append(n)

        return winning

    def get_points(self) -> int:
        point_sum = 0
        for i in range(len(self.have_win)):
            # first 2 numbers 1 point
            if i in [0, 1]:
                point_sum += pow(2, 0)
            else:
                point_sum += pow(2, i-1)

        return point_sum

class Pile():
    def __init__(self) -> None:
        # list of Card elems
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_points(self) -> int:
        point_sum = 0
        for card in self.cards:
            point_sum += card.get_points()

        return point_sum

def get_lines() -> list:
    # return list of lines
    with open("input.txt") as f:
        return f.readlines()

# matches everything behind ':'
look_behind = "(?<=:)[^\]]+"
# matches numbers
digits = "\d+"

def parse(card: str) -> Card:
    # string of all numbers separated by '|'
    number_str = re.findall(look_behind, card)[0]
    # split into winning and having numbers, then strip
    win_str, have_str = number_str.split(" | ")
    win_str  = win_str.strip()
    have_str = have_str.strip()
    # get numbers and turn them from str to int
    win_nums  = re.findall(digits, win_str)
    have_nums = re.findall(digits, have_str)
    win_nums  = [int(s) for s in win_nums]
    have_nums = [int(s) for s in have_nums]

    return Card(win_nums, have_nums)

def solution() -> int:
    pile  = Pile()
    lines = get_lines()
    for line in lines:
        # make card from line
        card = parse(line)
        # add to pile
        pile.add_card(card)
    return pile.get_points()

if __name__ == "__main__":
    result = solution()
    print(result)