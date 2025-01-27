from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class DiceRollForm(FlaskForm):
    dice_number = StringField("Dice number")
    dice_size = StringField("Dice size")
    roll = SubmitField("Roll")
