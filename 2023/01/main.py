# this is my first AoC puzzle, i could have
# done alot of things better
# after i finished i saw others using regex for
# finding words, but i dont know how to do that
# regex is scary

import re

VALID_NUMBERS = {
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

def get_str(s: str):
    word_nums = []
    for word, int_ in VALID_NUMBERS.items():
        [word_nums.append((m.start(), int_)) for m in re.finditer(word, s)]
    if word_nums:
        return get_end_values(word_nums)
    else:
        return None, None

def get_end_values(tl: list[tuple]):
    min_ = min(tl, key= lambda t: t[0])
    max_ = max(tl, key= lambda t: t[0])
    return min_, max_

def get_digit(s: str, reverse=False):
    for i, c in enumerate(s):
        try:
            if reverse:
                index = len(s) - 1 - i
            else:
                index = i
            return index, int(c)
        except Exception as e:
            continue

sum_ = 0
first_num = 0
last_num  = 0

with open("input.txt") as f:
    lines = f.readlines()
    # list of tuples that represent
    # (start_index, number_value)
    num_tuple_list = []
    for line in lines:
        reversed_ = line[:-1][::-1]
        # get first digit
        front_dig = get_digit(line)
        # get last digit
        end_dig  = get_digit(reversed_, reverse=True)
        # get first and last word numbers
        first_w, last_w = get_str(line)
        # append existing numbers and word numbers to list
        if front_dig: num_tuple_list.append(front_dig)
        if end_dig: num_tuple_list.append(end_dig)
        if first_w: num_tuple_list.append(first_w)
        if last_w: num_tuple_list.append(last_w)
        # find starting indexes of first and last num
        first_ind = min(num_tuple_list)[0]
        last_ind  = max(num_tuple_list)[0]
        # set tuple numeric values for mix and max index
        # for later addition to sum
        for num in num_tuple_list:
            if first_ind == num[0]:
                first_num = num[1]
                continue
            elif last_ind == num[0]:
                last_num = num[1]
        # hmm this doesnt look too good
        if first_ind == last_ind:
            sum_ += first_num * 10 + first_num
        else:
            sum_ += first_num * 10 + last_num
        # empty list for next iteration
        num_tuple_list = []

print(sum_)
