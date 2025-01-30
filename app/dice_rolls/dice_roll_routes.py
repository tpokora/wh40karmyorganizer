import logging

from flask import render_template, flash

from app.dice_rolls import bp
from app.dice_rolls.dice_roll_forms import DiceRollForm
from app.dice_rolls.dice_rolls import DiceRoll

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/dice_roll', methods=['GET', 'POST'])
def dice_rolls():
    form = DiceRollForm()
    if form.is_submitted():
        if not form.dice_number:
            flash('Dice number is required!')
        elif not form.dice_size:
            flash('Dice size is required!')
        roll_results = DiceRoll(f'{form.dice_number.data}d{form.dice_size.data}').roll()
        return render_template('dice_rolls/dice_roll.html', form=form, roll_results=roll_results)

    return render_template('dice_rolls/dice_roll.html', form=form)
