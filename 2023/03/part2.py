from part1 import *

def multiply(l: list[int]):
    prod = 1
    for i in l:
        prod *= i
    return prod

class Gear(Element):
    def __init__(self, row, index, string) -> None:
        super().__init__(row, index, string)

    def multiply_parts(self, first, second, third):
        first_numbers  = self.get_adjacent_numbers(first)
        second_numbers = self.get_adjacent_numbers(second)
        third_numbers  = self.get_adjacent_numbers(third)
        if self.has_two_parts(first_numbers, second_numbers, third_numbers):
            # list of number Element int values
            parts = []
            parts.extend(first_numbers)
            parts.extend(second_numbers)
            parts.extend(third_numbers)
            # print(f"parts: {parts}")
            # print(f"Product of {self}: {multiply(parts)}")
            return multiply(parts)

    def get_adjacent_numbers(self, numbers):
        # returns all number values adjacent to gear
        # number Element list
        row_numbers = []
        # int values of those Elems
        row_values  = []
        for num in numbers:
            for i in [self.index-1,self.index,self.index+1]:
                if i in num.index:
                    if num not in row_numbers:
                        row_numbers.append(num)
                        row_values.append(int(num.string))
        return row_values

    def has_two_parts(self, f, s, t):
        # return if exactly two values around gear
        return len(f) + len(s) + len(t) == 2

def split_stars(id_: int, number_list: list[tuple]) -> str:
    star_indexes = []
    for i, s in number_list:
        matches = re.finditer("[*]", s)
        # if any gears found, add them to list
        if matches:
            for m in matches:
                star_indexes.append(Gear(id_, i+m.start(), "*"))
    return star_indexes

def parse_file(lines):
    my_class = Lines()

    for id_, line in enumerate(lines, 1):
        # list of number Elements
        number_indexes = []
        line = line.strip()
        # list of tuples of elements with starting index and string value
        index_list = [(i, s) for i,s in enumerate(re.split("[.-]", line)) if s]
        index_list = fix_indexes(index_list)
        # list od Gears in row
        star_indexes = split_stars(id_, index_list)
        # cant remember, i think the fix_indexes above didnt properly fix
        # so i did it again here, should have done this in fix_indexes
        last_el_len = 0
        for i,s in enumerate(re.split("[.-]", line)):
            if s:
                i += last_el_len
                if s != "*":
                    number_indexes.extend(add_number(Element(id_, i, s)))
                last_el_len += len(s)
        my_class.num_ind_list.extend(number_indexes)
        my_class.sym_ind_list.extend(star_indexes)

    sum_ = 0
    for gear in my_class.sym_ind_list:
        first, second, third = my_class.get_rows(gear.row)
        product = gear.multiply_parts(first, second, third)
        # not all rows will have gears
        if product:
            sum_ += product
    return sum_

def solution() -> int:
    lines = get_lines()
    result = parse_file(lines)
    print(result)

if __name__ == "__main__":
    result = solution()