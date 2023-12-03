from part1 import *

class Gear(Element):
    def __init__(self, row, index, string) -> None:
        super().__init__(row, index, string)

    def multiply_gears(self, first, second, third):
        pass

    def has_two_gears(self):
        pass

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

if __name__ == "__main__":
    result = solution()