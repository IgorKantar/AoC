import re

def get_lines() -> list:
    # return list of lines
    with open("input.txt") as f:
        return f.readlines()

def solution() -> int:
    lines = get_lines()

if __name__ == "__main__":
    result = solution()