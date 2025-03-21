from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in
                self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random_cafe():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict()), 200


@app.route("/all")
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]), 200


@app.route("/search")
def find_cafe():
    location = request.args.get("loc")
    all_cafes = db.session.execute(db.select(Cafe).where(
        Cafe.location == location)).scalars().all()
    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes]), 200
    return jsonify(error={
        "Not Found": "Sorry, we don't have a cafe at that location.",
        }), 404


@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        has_sockets=bool(request.form.get("has_sockets")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfuly added a new Cafe"})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.session.get(Cafe, cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        return jsonify(response={
            "success": "Successfuly updated the price"
        }), 200
    return jsonify(error={
        "Not Found": "Sorry a cafe with that id was not found in the database."
    }), 404


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_to_delete = db.session.get(Cafe, cafe_id)
    if cafe_to_delete:
        if request.args.get("api-key") == "TopSecretAPI":
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={
                "success": "Successfuly deleted cafe"
            }), 200
        return jsonify(error="Sorry, that's not allowed. Make sure you have "
                             "the correct api_key"), 403
    return jsonify(error={
        "Not Found": "Sorry a cafe with that id was not found in the database."
    }), 404


if __name__ == '__main__':
    app.run(debug=True)
