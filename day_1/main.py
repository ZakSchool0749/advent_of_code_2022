"""advent of code day 1"""

def part_one(text: str):
    """ Calculates part one"""
    people_foods = text.split("\n\n")
    totals = list(map(lambda person: sum(int(val) for val in person.split()), people_foods))
    return max(totals)

def part_two(text: str):
    """ Calculates part two """
    people_foods = text.split("\n\n")
    totals = list(map(lambda person: sum(int(val) for val in person.split()), people_foods))
    totals.sort()
    return sum(totals[len(totals) - 3:len(totals)])

data = open("./day_1/input.txt", encoding="utf-8").read()

print(f"Part One: {part_one(data)}")
print(f"Part Two: {part_two(data)}")
