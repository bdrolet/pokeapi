from services.pokemon_service import PokemonService

def get_pokemon() -> None:
    service = PokemonService()
    result = service.get_pokemon("charmander")
    print(result)


if __name__ == "__main__":
    get_pokemon()