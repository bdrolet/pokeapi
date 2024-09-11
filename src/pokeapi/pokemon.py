from pokeapi.models.pokemon import Pokemon
from pokeapi.services.pokemon_service import pokemon_service

def get_pokemon(pokemon: str) -> Pokemon | None:
    """
    Get the pokemon with the given name or id
    :param pokemon: The name or id of the pokemon to get
    :returns models.pokemon.Pokemon: for the given name or id
    """
    return pokemon_service.get_pokemon(pokemon)
