import os
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import FloatField
from wtforms.validators import DataRequired
import requests

HEADERS_TMDB = {
    "accept": "application/json",
    "Authorization": os.environ.get("BEARER_TOKEN")
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
db.init_app(app)


class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True,
                                       nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def __repr__(self):
        return f"<Movie: {self.title}>"


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = FloatField(label="Your rating out of 10 (e.g. 7.5)")
    review = StringField(label="Your review")
    submit = SubmitField(label="Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for n in range(len(all_movies)):
        all_movies[n].ranking = len(all_movies) - n
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    rate_movie_form = RateMovieForm()
    if rate_movie_form.validate_on_submit():
        movie = db.get_or_404(Movie, request.args.get("id"))
        movie.rating = float(rate_movie_form.rating.data)
        movie.review = rate_movie_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=rate_movie_form)


@app.route("/delete")
def delete_movie():
    movie = db.get_or_404(Movie, request.args.get("id"))
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/find", methods=["GET", "POST"])
def find_movie():
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        param = {
            "query": add_movie_form.title.data,
        }
        response = requests.get("https://api.themoviedb.org/3/search/movie",
                                headers=HEADERS_TMDB, params=param)
        response.raise_for_status()
        movie_data = response.json()["results"]
        return render_template("select.html",
                               movie_data=movie_data)
    return render_template("add.html", form=add_movie_form)


@app.route("/add")
def add_movie():
    movie_id = request.args.get("id")
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}",
                            headers=HEADERS_TMDB)
    response.raise_for_status()
    movie = response.json()
    new_movie = Movie(
        title=movie["title"],
        year=movie["release_date"][:4],
        description=movie["overview"],
        img_url=f"https://image.tmdb.org/t/p/original{movie["poster_path"]}",
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("rate_movie", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
