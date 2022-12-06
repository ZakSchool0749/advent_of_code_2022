"""advent of code day 4"""

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part_one(text: str):
    """ Calculates part one"""
    score = 0
    for line in text.splitlines():
        string1 = line[0:len(line)//2]
        string2 = line[len(line)//2:]
        res = is_sharing(string1, string2)
        if res:
            score += letters.find(res) + 1
    return score


def is_sharing(pt1, pt2):
    for letter1 in pt1:
        for letter2 in pt2:
            if letter1 == letter2:
                return letter1

    return False

def part_two(text: str):
    """ Calculates part two """
    score = 0
    lines = text.splitlines()

    for i in range(int((len(lines) / 3))):
        res = sharing_3((lines[i * 3], lines[(i*3) + 1], lines[(3*i) + 2]))

        if res:
            score += letters.find(res) + 1

    return score
    

def sharing_3(chunk):
    for c1 in chunk[0]:
        for c2 in chunk[1]:
            for c3 in chunk[2]:
                if c1 == c2 and c2 == c3:
                    return c1

data = open("./day_3/input.txt", encoding="utf-8").read()

# print(f"Part One: {part_one(data)}")
print(f"Part Two: {part_two(data)}")
