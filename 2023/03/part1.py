SYMBOLS = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","/",",","[","]","{","}","\\", "|","'","\"",";",":","<",">","?"]
import re

class Element():
    def __init__(self, row, index, string) -> None:
        self.row = row
        self.index  = index
        self.string = string

    def __repr__(self) -> str:
        return (f"{self.row} {self.index} {self.string}")

class Lines():
    def __init__(self) -> None:
        self.added_numbers = []
        self.num_ind_list = []
        self.sym_ind_list = []

    def check(self):
        for star in self.sym_ind_list:
            self.check_circle(star)
        # print(self.added_numbers)

    def check_circle(self, star: Element):
        first, second, third = self.get_rows(star.row)
        # print(first)
        self.check_row(first, star)
        self.check_row(second, star)
        self.check_row(third, star)

    def check_row(self, num_row, star):
        for num in num_row:
            for i in [star.index-1,star.index,star.index+1]:
                if i in num.index:
                    # print(num)
                    if num not in self.added_numbers:
                        # print(num)
                        self.added_numbers.append(num)

    def get_numbers(self):
        return sum([int(n.string) for n in self.added_numbers])

    def get_rows(self, row_id):
        first  = []
        second = []
        third  = []
        for num in self.num_ind_list:
            if num.row == row_id - 1:
                first.append(num)
            if num.row == row_id:
                # print(num)
                second.append(num)
            if num.row == row_id + 1:
                third.append(num)
        return first, second, third

def get_lines() -> list:
    # return list of lines
    with open("input.txt") as f:
        return f.readlines()

def sym_to_star(line) -> str:
    return re.sub("[-`~!@#$%^&*()_+=/\|]", "*", line)

def split_stars(id_: int, number_list: list[tuple]) -> str:
    star_indexes = []
    for i, s in number_list:
        matches = re.finditer("[*]", s)
        for m in matches:
            star_indexes.append(Element(id_, i+m.start(), "*"))
    return star_indexes

def fix_indexes(index_list: list[tuple]):
    sum_ = 0
    index_list2 = []
    for ind, s in index_list:
        index_list2.append((ind+sum_, s))
        sum_ += len(s)
    return index_list2

def get_indexes(start, len_):
    return [i for i in range(start, start+len_)]

def add_number(el: Element) -> list:
    # if multiple umbers stuck togetehr by star
    multi_string = False
    if "*" in el.string:
        multi_string = el.string.split("*")[1]
    if multi_string:
        first_num  = el.string.split("*")[0]
        # print(f"el: {el} first: {first_num} multi: {multi_string}")
        second_num = el.string.split("*")[1]
        result_list = []
        if first_num:
            first_el  = Element(el.row, get_indexes(el.index, len(first_num)), first_num)
            result_list.append(first_el)
        if second_num:
            second_el = Element(el.row, get_indexes(el.index+len(first_num)+1, len(second_num)), second_num)
            result_list.append(second_el)
        if el.row == 137:
            print(f"FAS: {result_list}")
        return result_list
    else:
        s = el.string.replace("*", "")
        if el.row == 137:
            print(f"FAS: {Element(el.row, get_indexes(el.index, len(s)), s)}")
        return [Element(el.row, get_indexes(el.index, len(s)), s)]

def parse_file(lines):
    my_class = Lines()

    for id_, line in enumerate(lines, 1):
        number_indexes = []
        line = line.strip()
        line = sym_to_star(line)
        index_list = [(i, s) for i,s in enumerate(re.split("[.-]", line)) if s]
        index_list = fix_indexes(index_list)
        star_indexes = split_stars(id_, index_list)
        last_el_len = 0
        # print(re.split("[.-]", line))
        for i,s in enumerate(re.split("[.-]", line)):
            if s:
                i += last_el_len
                if s != "*":
                    number_indexes.extend(add_number(Element(id_, i, s)))
                last_el_len += len(s)
        # print(number_indexes)
        # print(star_indexes)
        my_class.num_ind_list.extend(number_indexes)
        # print(my_class.num_ind_list)
        my_class.sym_ind_list.extend(star_indexes)
        # print(my_class.sym_ind_list)

    my_class.check()
    x = [(n.row, n.string) for n in my_class.added_numbers]
    x = sorted(x, key=lambda n: n[0])
    # for y in my_class.num_ind_list:
    #     if y.row == 139:
    #         print(y)
    # print(x)
    print(my_class.get_numbers())

def solution() -> int:
    lines = get_lines()
    parse_file(lines)

if __name__ == "__main__":
    result = solution()