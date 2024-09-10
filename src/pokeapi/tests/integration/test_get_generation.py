from pokeapi.services.pokemon_service import PokemonService


def test_get_pokemon() -> None:
    service = PokemonService()
    result = service.get_generation("generation-i")
    assert result is not None
    print(result)
        

