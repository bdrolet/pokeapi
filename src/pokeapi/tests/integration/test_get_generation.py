from pokeapi.generation import get_generation


def test_get_pokemon() -> None:
    result = get_generation("generation-i")
    assert result is not None
    print(result)
        

