from pokeapi.models.pokemon import Pokemon
import requests


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

class PokemonService:
    base_url = "https://pokeapi.co/api/v2/"

    def get_pokemon(self, pokemon_id: str) -> Pokemon | None:
        """
        Calls the pokeapi to get the pokemon with the given id
        See docs for the reaqest here: https://pokeapi.co/docs/v2#pokemon
        :param pokemon_id: The id or name of the pokemon to get
        :returns models.pokemon.Pokemon: for the given id or name
        """
        url: str = f"{self.base_url}/pokemon/{pokemon_id}"
        try:
            resp = requests.get(url)
            resp.raise_for_status()  # Raise an exception if the request was unsuccessful
        except Exception as e:
            # Handle the exception here
            print(f"An error while requesting pokemon {pokemon_id}: {e}")
            return None
        try:
            data = resp.json()
        except Exception as e:
            print(f"And error while parsing json while requesting json for {pokemon_id} : {e}")
            return None
        
        pokemon: Pokemon = _to_pokemon(data)
        return pokemon