from flask import Flask, render_template
from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post = Post()
    return render_template("index.html", posts=post.all_posts)


@app.route("/post/<int:post_id>")
def get_post(post_id):
    post = Post()
    post_selected = post.fetch_post(post_id)
    return render_template("post.html", post=post_selected)


if __name__ == "__main__":
    app.run(debug=True)
