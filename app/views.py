from flask import render_template, request, flash
from flask_wtf import FlaskForm
from app import app
import pandas as pd
from models import heart_failure

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = FlaskForm()

    if request.method == 'POST':

        age = request.form.get('age')
        sex = request.form.get('sex')
        chest_pain = request.form.get('chest-pain')
        maxHR = request.form.get('max-HR')
        restingBP = request.form.get('resting-BP')
        exerciseAngina = 'Y' if request.form.get('angina') != None else 'N'

        for feat in [age, sex, chest_pain, maxHR, restingBP, exerciseAngina]:
            if not feat:
                flash("Есть пустые поля! Необходимо заполнить все поля!!!")
                return render_template("index.html", title='Home', form=form)

        X = pd.DataFrame(
            [[age, sex, chest_pain, maxHR, restingBP, exerciseAngina]],
            columns=['Age', 'Sex', 'ChestPainType', 'MaxHR', 'RestingBP', 'ExerciseAngina']
        )
        if heart_failure.predict_proba(X)[:, 1][0] > 0.425:
            flash("Высокая вероятность сердечной недостаточности!")
        else:
            flash("Низкая вероятность сердечной недостаточности!")

    return render_template("index.html", title='Home', form=form)

