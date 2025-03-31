from flask import (Flask, render_template, request, url_for, redirect, flash,
                   send_from_directory)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (UserMixin, login_user, LoginManager, login_required,
                         current_user, logout_user)

app = Flask(__name__)
app.config["SECRET_KEY"] = "0c7d94530d8389d0cc0f9796d907f71d2be6ec0bc466f"
login_manager = LoginManager()
login_manager.init_app(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def user_loader(user_id):
    return db.session.get(User, user_id)


@app.route('/')
def home():
    return render_template("index.html",
                           logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = db.session.execute(
            db.select(User).where(User.email == request.form["email"])
        ).scalar()
        if user:
            flash("Email already registered. Please log in instead.")
            return redirect(url_for("login"))

        hash_and_salted_password = generate_password_hash(
            password=request.form["password"],
            method="pbkdf2:sha256",
            salt_length=8,
        )
        new_user = User(
            email=request.form["email"],
            password=hash_and_salted_password,
            name=request.form["name"]
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("secrets"))
    return render_template("register.html",
                           logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = db.session.execute(
            db.select(User).where(User.email == request.form["email"])
        ).scalar()
        if user:
            if check_password_hash(user.password, request.form["password"]):
                login_user(user)
                return redirect(url_for("secrets"))
            flash("Invalid password. Please try again.")
            return redirect(url_for("login"))
        flash("Email does not exist. Please try again.")
        return redirect(url_for("login"))
    return render_template("login.html",
                           logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name,
                           logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static",
                               path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
