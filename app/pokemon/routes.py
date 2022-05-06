from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required
import requests as r


pokemon = Blueprint('pokemon', __name__, template_folder="pokemon_templates")

from app.models import db, Pokemon, Pokedex
from .forms import CreatePokemonForm

@pokemon.route('/pokemon', methods=["POST"])
def myPokemon():
    name = request.form.to_dict()['name']
    data = r.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    if data.status_code == 200:
        my_data = data.json()
        abilities = my_data['abilities']
        my_abilities = []
        count = 1
        for item in abilities:
            print(item['ability']['name'])
            my_abilities.append((item['ability']['name']))
            my_img = my_data['sprites']['front_default']
        pokemon = Pokemon.query.filter_by(pokemon_name=name).first()
        if pokemon is None:
            pokemon = Pokemon(name, my_img)
            db.session.add(pokemon)
            db.session.commit()
        return render_template('pokemon.html', img_url=my_img, name=name, pokemon=pokemon)
    return redirect(url_for('home'))

@pokemon.route('/pokedex')
@login_required
def showPokedex():
    pokedex = Pokedex.query.filter_by(user_id=current_user.id)


