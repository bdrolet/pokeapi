from pokeapi.models.pokemon import Pokemon
from pokeapi.models.generation import Generation
import requests

class PokemonService:
    """
    A service class to interact with the pokeapi
    See: https://pokeapi.co/docs/v2
    """
    base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon(self, pokemon_id: str) -> Pokemon | None:
        """
        Calls the pokeapi to get the pokemon with the given id or name
        See docs for the reaqest here: https://pokeapi.co/docs/v2#pokemon
        :param pokemon_id: The id or name of the pokemon to get
        :returns models.pokemon.Pokemon: for the given id or name
        """
        url: str = f"{self.base_url}/pokemon/{pokemon_id}"

        # Get the pokemon data from the pokeapi
        try:
            resp = requests.get(url)
            resp.raise_for_status()  # Raise an exception if the request was unsuccessful
        except Exception as e:
            # Handle the exception here
            print(f"An error while requesting pokemon {pokemon_id}: {e}")
            return None
        
        # Parse the json data
        try:
            data = resp.json()
        except Exception as e:
            print(f"And error while parsing json while requesting json for {pokemon_id} : {e}")
            return None
        
        pokemon: Pokemon = _to_pokemon(data)
        return pokemon
    
    def get_generation(self, genration: str) -> Generation | None:
        """
        Calls the pokeapi to get the generation with the given id or name
        See docs for the reaqest here: https://pokeapi.co/docs/v2#generation
        :param generation: The id or name of the generation to get
        :returns pokeapi.models.generation.Generation: for the given id or name
        """
        url: str = f"{self.base_url}/generation/{genration}"

        # Get the generation data from the pokeapi
        try:
            resp = requests.get(url)
            resp.raise_for_status()  # Raise an exception if the request was unsuccessful
        except Exception as e:
            # Handle the exception here
            print(f"An error while requesting pokemon {genration}: {e}")
            return None
        
        # Parse the json data
        try:
            data = resp.json()
        except Exception as e:
            print(f"And error while parsing json while requesting json for {genration} : {e}")
            return None
        
        genration: Generation = _to_generation(data)
        return genration
    

def _to_pokemon(pokemon: dict) -> Pokemon:
    return Pokemon(
        id=pokemon["id"],
        name=pokemon["name"],
        height=pokemon["height"],
        weight=pokemon["weight"],
        base_experience=pokemon["base_experience"],
        is_default=pokemon["is_default"],
        order=pokemon["order"],
        abilities=pokemon["abilities"],
        forms=pokemon["forms"],
        game_indices=pokemon["game_indices"],
        held_items=pokemon["held_items"],
        location_area_encounters=pokemon["location_area_encounters"],
        moves=pokemon["moves"],
        past_types=pokemon["past_types"],
        sprites=pokemon["sprites"],
        cries=pokemon["cries"],
        species=pokemon["species"],
        stats=pokemon["stats"],
        types=pokemon["types"]
    )

def _to_generation(generation: dict) -> Generation:
    return Generation(
        id=generation["id"],
        name=generation["name"],
        abilities=generation["abilities"] if generation["abilities"] else [],
        names=generation["names"] if "names" in generation else [],
        main_region=generation["main_region"] if "main_region" in generation else {},
        moves=generation["moves"] if "moves" in generation else [],
        pokemon_species=generation["pokemon_species"] if "pokemon_species" in generation else [],
        types=generation["types"] if "types" in generation else [],
        version_groups=generation["version_groups"] if "version_groups" in generation else []
    )