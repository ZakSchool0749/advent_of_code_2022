"""advent of code day 2"""

from enum import Enum


def move_from_char(character: str):
    """ Gives the move repersentation of the a char """
    match character:
        case "A" | "X":
            return Move.ROCK
        case "B" | "Y":
            return Move.PAPER
        case "C" | "Z":
            return Move.SCISSORS
        case _:
            print(character, len(character))


def result_from_char(character: str):
    match character:
        case "X":
            return MoveResult.LOOSE
        case "Y":
            return MoveResult.DRAW
        case "Z":
            return MoveResult.WIN
        case _:
            print(character, len(character))

    


class MoveResult(Enum):
    WIN = 6
    DRAW = 3
    LOOSE = 0

    def get_player(self, other):
        if self.name == "DRAW":
            return other
        elif self.name == "WIN":
            if other.name == "ROCK":
                return Move.PAPER
            elif other.name == "PAPER":
                return Move.SCISSORS
            else:
                return Move.ROCK
        else:
            if other.name == "ROCK":
                return Move.SCISSORS
            elif other.name == "PAPER":
                return Move.ROCK
            else:
                return Move.PAPER
            



class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def cmp(self, other):
        if self.name == other.name:
            return MoveResult.DRAW
        elif (self.name == "ROCK" and other.name == "SCISSORS") or (self.name == "PAPER" and other.name == "ROCK") or (self.name == "SCISSORS" and other.name == "PAPER"):
            return MoveResult.WIN
        else:
            return MoveResult.LOOSE


def part_one(text: str):
    """ Calculates part one"""
    score = 0
    for line in text.splitlines():
        [responce, _, move] = line.partition(" ")
        move = move_from_char(move)
        responce = move_from_char(responce)

        score += move.value + move.cmp(responce).value

    return score


def part_two(text: str):
    """ Calculates part two """
    score = 0
    for line in text.splitlines():
        [responce, _, result] = line.partition(" ")
        responce = move_from_char(responce)
        result = result_from_char(result)
        move = result.get_player(responce)

        score += result.value + move.value

    return score


data = open("./day_2/example.txt", encoding="utf-8").read()

print(f"Part One: {part_one(data)}")
print(f"Part Two: {part_two(data)}")
