import re
# 53 868
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
x = 0
with open("input.txt") as f:
    lines = f.readlines()
    num_tuple_list = []
    for line in lines:
        reversed_ = line[:-1][::-1]
        front_dig = get_digit(line)
        end_dig  = get_digit(reversed_, reverse=True)
        first_w, last_w = get_str(line)
        if front_dig: num_tuple_list.append(front_dig)
        if end_dig: num_tuple_list.append(end_dig)
        if first_w: num_tuple_list.append(first_w)
        if last_w: num_tuple_list.append(last_w)
        first_ind = min(num_tuple_list)[0]
        last_ind  = max(num_tuple_list)[0]
        for num in num_tuple_list:
            if first_ind == num[0]:
                first_num = num[1]
                continue
            elif last_ind == num[0]:
                last_num = num[1]
        if first_ind == last_ind:
            a = first_num * 10 + first_num
            sum_ += a
        else:
            a = first_num * 10 + last_num
            sum_ += a
        num_tuple_list = []

print(sum_)
