from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True,
                                       nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class PostForm(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    author = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Image URL", validators=[DataRequired(),
                                                              URL()])
    body = CKEditorField('Body', validators=[DataRequired()])
    submit = SubmitField(label="SUBMIT POST")


@app.route("/")
def get_all_posts():
    posts = db.session.execute(
        db.select(BlogPost).order_by(BlogPost.id)
    ).scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/show/<int:post_id>")
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        blog_post = BlogPost(
            title=post_form.title.data,
            subtitle=post_form.subtitle.data,
            date=date.today().strftime("%B %d, %Y"),
            author=post_form.author.data,
            img_url=post_form.img_url.data,
            body=post_form.body.data
        )
        db.session.add(blog_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=post_form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post_to_update = db.get_or_404(BlogPost, post_id)
    edit_form = PostForm(title=post_to_update.title,
                         subtitle=post_to_update.subtitle,
                         author=post_to_update.author,
                         img_url=post_to_update.img_url,
                         body=post_to_update.body)
    if edit_form.validate_on_submit():
        post_to_update.title = edit_form.title.data
        post_to_update.subtitle = edit_form.subtitle.data
        post_to_update.author = edit_form.author.data
        post_to_update.img_url = edit_form.img_url.data
        post_to_update.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_update.id))
    return render_template("make-post.html", form=edit_form,
                           post=post_to_update)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
