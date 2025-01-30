import logging

from flask import render_template, flash, request

from app.dice_rolls import bp
from app.dice_rolls.dice_roll_forms import DiceRollForm
from app.dice_rolls.dice_rolls import DiceRoll

ROLLS_DICE_ROLL_HTML_TEMPLATE = 'dice_rolls/dice_roll.html'

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(message)s')


@bp.route('/dice_roll', methods=['GET', 'POST'])
def dice_rolls() -> str:
    form = DiceRollForm()
    if request.method == 'POST':
        return __handle_form(form)

    return render_template(ROLLS_DICE_ROLL_HTML_TEMPLATE, form=form)


def __handle_form(form) -> str:
    if form.validate_on_submit():
        roll_results = DiceRoll(f'{form.dice_number.data}d{form.dice_size.data}').roll()
        return render_template(ROLLS_DICE_ROLL_HTML_TEMPLATE, form=form, roll_results=roll_results)
    else:
        if form.dice_number.errors:
            flash(form.dice_number.errors[0])
        if form.dice_size.errors:
            flash(form.dice_size.errors[0])
        return render_template(ROLLS_DICE_ROLL_HTML_TEMPLATE, form=form)

