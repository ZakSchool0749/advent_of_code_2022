"""advent of code day 3"""

def part_one(text: str):
    """ Calculates part one"""
    full_overaps = 0

    for line in text.splitlines():
        [range_one, range_two] = list(map(lambda r:r.split("-"), line.split(",")))

        range_one = [int(range_one[0]), int(range_one[1])]
        range_two = [int(range_two[0]), int(range_two[1])]

        if (range_one[0] <= range_two[0] and range_one[1] >= range_two[1]) or (range_two[0] <= range_one[0] and range_two[1] >= range_one[1]):
            full_overaps += 1

    return full_overaps

def semi_overlapping(range_one, range_two):
    for x in range(range_one[0], range_one[1] + 1):
        for y in range(range_two[0], range_two[1] + 1):
            if x == y:
                return True

    return False


def part_two(text: str):
    """ Calculates part two """
    overlaps = 0

    for line in text.splitlines():
        [range_one, range_two] = list(map(lambda r:r.split("-"), line.split(",")))

        range_one = [int(range_one[0]), int(range_one[1])]
        range_two = [int(range_two[0]), int(range_two[1])]

        print(range_one, range_two, semi_overlapping(range_one, range_two))

        if semi_overlapping(range_one, range_two):
            overlaps += 1 

        

    return overlaps
    

data = open("./day_4/input.txt", encoding="utf-8").read()

print(f"Part One: {part_one(data)}")
print(f"Part Two: {part_two(data)}")
