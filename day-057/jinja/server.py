from flask import Flask, render_template
import requests
import random
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess/<string:name>")
def guess(name):
    parameter = {
        "name": name
    }

    gender_data = requests.get("https://api.genderize.io",
                               params=parameter).json()
    age_data = requests.get("https://api.agify.io",
                            params=parameter).json()

    return render_template("guess.html",
                           person_name=name,
                           gender=gender_data["gender"],
                           age=age_data["age"])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
