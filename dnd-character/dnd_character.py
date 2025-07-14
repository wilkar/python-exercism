from math import floor
from random import randint


class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self) -> list[int]:
        scores = sorted(randint(1, 6) for _ in range(4))
        return sum(scores[1:])


def modifier(value: int) -> int:
    return floor((value - 10) / 2)
