import re

class Element():
    """Class representing part number or symbol."""

    def __init__(self, row, index, string) -> None:
        # row of element
        self.row = row
        # list of indexes of self.string chars
        self.index  = index
        # str value of elem
        self.string = string

    def __repr__(self) -> str:
        return (f"{self.row} {self.index} {self.string}")

# should have named this differently
class Lines():
    """Class used for solution methods."""

    def __init__(self) -> None:
        self.added_numbers = []
        # lists of Elements()
        self.num_ind_list = []
        self.sym_ind_list = []

    def check(self):
        for star in self.sym_ind_list:
            self.check_circle(star)

    def check_circle(self, star: Element):
        # check adjacent fields of current
        # and two closest rows
        first, second, third = self.get_rows(star.row)
        self.check_row(first, star)
        self.check_row(second, star)
        self.check_row(third, star)

    def check_row(self, num_row, star):
        for num in num_row:
            for i in [star.index-1,star.index,star.index+1]:
                # if num contains adjacent index,
                # check if already added and add if not
                if i in num.index:
                    if num not in self.added_numbers:
                        self.added_numbers.append(num)

    def get_numbers(self):
        # return int values of number Elements
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
    # change all symbols to star,
    # but i dont think this was needed
    # as part 2 solution shows
    return re.sub("[-`~!@#$%^&*()_+=/\|]", "*", line)

def split_stars(id_: int, number_list: list[tuple]) -> str:
    # if star is sticking to number string, make new Element
    # with new index for that star
    star_indexes = []
    for i, s in number_list:
        matches = re.finditer("[*]", s)
        for m in matches:
            star_indexes.append(Element(id_, i+m.start(), "*"))
    return star_indexes

def fix_indexes(index_list: list[tuple]):
    # since re.split removes "." symbols,
    # increment indexes by number of "." removed before it
    sum_ = 0
    index_list2 = []
    for ind, s in index_list:
        index_list2.append((ind+sum_, s))
        sum_ += len(s)
    return index_list2

def get_indexes(start, len_):
    # indexes a number string occupies
    return [i for i in range(start, start+len_)]

def add_number(el: Element) -> list:
    # if multiple numbers stuck together by star
    multi_string = False
    if "*" in el.string:
        multi_string = el.string.split("*")[1]
    if multi_string:
        first_num  = el.string.split("*")[0]
        second_num = el.string.split("*")[1]
        result_list = []
        if first_num:
            first_el  = Element(el.row, get_indexes(el.index, len(first_num)), first_num)
            result_list.append(first_el)
        if second_num:
            second_el = Element(el.row, get_indexes(el.index+len(first_num)+1, len(second_num)), second_num)
            result_list.append(second_el)
        return result_list
    else:
        s = el.string.replace("*", "")
        return [Element(el.row, get_indexes(el.index, len(s)), s)]

def parse_file(lines):
    my_class = Lines()

    for id_, line in enumerate(lines, 1):
        # really should name things better
        # list of number Elements
        number_indexes = []
        line = line.strip()
        line = sym_to_star(line)
        # list of tuples of elements with starting index and string value
        index_list = [(i, s) for i,s in enumerate(re.split("[.-]", line)) if s]
        index_list = fix_indexes(index_list)
        star_indexes = split_stars(id_, index_list)
        # cant remember, i think the fix_indexes above didnt properly fix
        # so i did it again here
        last_el_len = 0
        for i,s in enumerate(re.split("[.-]", line)):
            if s:
                i += last_el_len
                if s != "*":
                    number_indexes.extend(add_number(Element(id_, i, s)))
                last_el_len += len(s)
        my_class.num_ind_list.extend(number_indexes)
        my_class.sym_ind_list.extend(star_indexes)

    # should have named this start and get_sum
    my_class.check()
    print(my_class.get_numbers())

def solution() -> int:
    lines = get_lines()
    parse_file(lines)

if __name__ == "__main__":
    result = solution()