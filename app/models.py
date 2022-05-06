
# models.py controls the communications btw the controller & db. Usually use ORM (Object Relational Mapper)
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin


db = SQLAlchemy()

# create our models based off of our ERD

class User(db.Model, UserMixin ):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref='author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

class Post(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(300))
    caption = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, image, caption):
        self.title = title
        self.image = image
        self.caption = caption

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False, unique=False)
    image = db.Column(db.String(300))
    description = db.Column(db.String(300))
    price = db.Column(db.Float())
    cart_item = db.relationship('Cart', backref='cart_product', lazy=True)

    def __init__(self, product_name, image, description, price):
        self.product_name = product_name
        self.image = image
        self.description = description
        self.price = price

def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "image": self.image,
            "description": self.description,
            "price": self.price
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __init__(self, user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String(50))
    img_url = db.Column(db.String(300))
    ability1 = db.Column(db.String(300))
    ability2 = db.Column(db.String(300))
    pokedex_pokemon = db.relationship('Pokedex', backref='pokedex_pokemon', lazy=True)

    def __init__(self, pokemon_name, img_url):
        self.pokemon_name = pokemon_name
        self.img_url = img_url

    def to_dict(self):
        return {
            "id": self.id,
            "pokemon_name": self.pokemon_name,
            "img_url": self.img_url,
        }

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), nullable=False)

    def __init__(self, user_id, pokemon_id):
        self.user_id = user_id
        self.pokemon_id = pokemon_id