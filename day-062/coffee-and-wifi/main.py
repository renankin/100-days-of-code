from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = URLField("Cafe Location on Google Maps (URL)",
                        validators=[DataRequired(), URL()])
    opening_time = StringField("Opening Time e.g. 8AM",
                               validators=[DataRequired()])
    closing_time = StringField("Closing Time e.g. 5:30PM",
                               validators=[DataRequired()])
    coffee_emoji = ["☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    coffee_rating = SelectField(
        label="Coffee Rating",
        validators=[DataRequired()],
        choices=[(emoji, emoji) for emoji in coffee_emoji]
    )
    strength_emoji = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    wifi_rating = SelectField(
        label="Wifi Strength Rating",
        validators=[DataRequired()],
        choices=[(emoji, emoji) for emoji in strength_emoji]
    )
    socket_emoji = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    socket_availability = SelectField(
        label="Power Socket Availability",
        validators=[DataRequired()],
        choices=[(emoji, emoji) for emoji in socket_emoji]
    )
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(
                "cafe-data.csv", mode="a", newline="", encoding="utf-8"
        ) as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            cafe_data = [
                form.cafe.data, form.location.data,
                form.opening_time.data, form.closing_time.data,
                form.coffee_rating.data, form.wifi_rating.data,
                form.socket_availability.data,
            ]
            csv_writer.writerow(cafe_data)

    return render_template("add.html", form=form)


@app.route('/cafes')
def cafes():
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_reader:
            list_of_rows.append(row)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
