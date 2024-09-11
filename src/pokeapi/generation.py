from pokeapi.models.generation import Generation
from pokeapi.services.pokemon_service import pokemon_service

def get_generation(generation: str) -> Generation | None:
    """
    Get the generation with the given name or id
    :param generation: The name or id of the generation to get
    :returns models.generation.Generation: for the given name or id
    """
    return pokemon_service.get_generation(generation)

