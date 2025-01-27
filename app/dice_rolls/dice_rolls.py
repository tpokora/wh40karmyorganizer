import random
import re


class DiceRoll:

    __pattern = r'^\d+d\d+$'

    def __init__(self, dice_roll):
        if not re.match(self.__pattern, dice_roll):
            raise ValueError("Incorrect format")
        split = dice_roll.split("d")
        self.number_of_dice = split[0]
        self.dice_value = split[1]

    def roll(self) -> list[int]:
        return [random.randrange(1, int(self.dice_value)) for _ in range(0, int(self.number_of_dice))]

