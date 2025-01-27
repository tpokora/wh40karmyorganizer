import unittest

from app.dice_rolls.dice_rolls import DiceRoll


class DiceRollTest(unittest.TestCase):

    @staticmethod
    def test_dice_roll_should_return_two_numbers():
        # given
        dice_roll = "2d6"

        # when
        roll_result = DiceRoll(dice_roll).roll()

        # then
        assert len(roll_result) == 2
        for value in roll_result:
            assert value > 0
            assert value <= 6

    def test_dice_roll_should_raise_exception_for_incorrect_format(self):
        # given
        dice_roll = "2dx"

        # expect
        with self.assertRaisesRegexp(ValueError, "Incorrect format"):
            DiceRoll(dice_roll).roll()


