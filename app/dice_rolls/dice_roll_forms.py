from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class DiceRollForm(FlaskForm):
    dice_number = StringField("Dice number", validators=[DataRequired()])
    dice_size = StringField("Dice size", validators=[DataRequired()])
    roll = SubmitField("Roll")

    def validate_dice_number(self, field):
        if not field.data.isdigit():
            raise ValidationError("Dice number must be a numeric value")

    def validate_dice_size(self, field):
        if not field.data.isdigit():
            raise ValidationError("Dice size must be a numeric value")
