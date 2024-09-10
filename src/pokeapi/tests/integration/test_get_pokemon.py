
from pokeapi.services.pokemon_service import PokemonService


def test_get_pokemon() -> None:
    service = PokemonService()
    result = service.get_pokemon("charmander")
    assert result is not None
    assert result.name == "charmander"
    assert result.id == 4
        

