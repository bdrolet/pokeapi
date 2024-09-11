
from pokeapi.pokemon import get_pokemon


def test_get_pokemon() -> None:
    result = get_pokemon("charmander")
    assert result is not None
    assert result.name == "charmander"
    assert result.id == 4
        

