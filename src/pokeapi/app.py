from flask import Flask, jsonify
from dataclasses import asdict

from pokeapi.services.pokemon_service import PokemonService
from pokeapi.models.pokemon import Pokemon
from pokeapi.models.generation import Generation

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping() -> str:
    return "pong"

@app.route("/pokemon/<name>", methods=["GET"])
def get_pokemon(name: str) -> Pokemon:
    service = PokemonService()
    pokemon: Pokemon = service.get_pokemon(name)
    return jsonify(asdict(pokemon))

@app.route("/generation/<name>", methods=["GET"])
def get_generation(name: str) -> dict:
    service = PokemonService()
    generation: Generation = service.get_generation(name)