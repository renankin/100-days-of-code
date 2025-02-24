from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USERNAME = os.environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

posts = requests.get("https://api.npoint.io/de42e29481a56d88c0e6").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_USERNAME, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_USERNAME,
                to_addrs=EMAIL_USERNAME,
                msg=f"Subject:New Message\n\n"
                    f"Name: {request.form["name"]}\n"
                    f"Email: {request.form["email"]}\n"
                    f"Phone: {request.form["phone"]}\n"
                    f"Message: {request.form["message"]}"
            )
        return render_template("contact.html",
                               message="Successfuly sent the message")
    return render_template("contact.html", message="Contact Me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
