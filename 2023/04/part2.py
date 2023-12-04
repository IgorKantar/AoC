import re

class Card():
    def __init__(self, row_id: int, winning:list[int], have:list[int]) -> None:
        # card id
        self.row_id  = row_id
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

    # not needed this time
    def get_points(self) -> int:
        point_sum = 0
        for i in range(len(self.have_win)):
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

    # not needed this time
    def get_points(self) -> int:
        point_sum = 0
        for card in self.cards:
            point_sum += card.get_points()

        return point_sum

    def recursion(self, cards: list[Card]) -> list:
        # stopping step
        if not cards:
            return []
        # list of additional cards
        copy_card_list = []
        for card in cards:
            # if winning card
            if card.have_win:
                # should have made all this into method
                # add len(card.have_win) cards to copy list
                start = card.row_id+1
                end = start + len(card.have_win)
                if end > len(self.cards):
                    end = len(self.cards)
                copy_card_list.extend(self.get_copies(start, end))
        # recursive step, but this time loop over additional cards
        # won from 'cards' list
        return copy_card_list + self.recursion(copy_card_list)

    def get_total_cards(self) -> int:
        # get list of additional collected cards
        all_copies = self.recursion(self.cards)
        # return overall number of cards
        return len(self.cards) + len(all_copies)

    def get_copies(self, start: int, end: int):
        return [self.cards[i] for i in range(start, end)]

def get_lines() -> list:
    # return list of lines
    with open("input.txt") as f:
        return f.readlines()

# matches everything behind ':'
look_behind = "(?<=:)[^\]]+"
# matches numbers
digits = "\d+"

def parse(row_id: int, card: str) -> Card:
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
    # this time add row_id
    return Card(row_id, win_nums, have_nums)

def solution() -> int:
    pile  = Pile()
    lines = get_lines()
    for i, line in enumerate(lines):
        # make card from line
        card = parse(i, line)
        # add to pile
        pile.add_card(card)
    # could have done this in one line
    total_cards = pile.get_total_cards()
    return total_cards

if __name__ == "__main__":
    result = solution()
    print(result)