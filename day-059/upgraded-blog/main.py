from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)

post_data = requests.get("https://api.npoint.io/de42e29481a56d88c0e6").json()


@app.route("/")
def home():
    return render_template("index.html", posts=post_data)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<int:post_id>")
def get_post(post_id):
    for available_post in post_data:
        if available_post["id"] == post_id:
            return render_template("post.html", post=available_post)


if __name__ == "__main__":
    app.run(debug=True)
