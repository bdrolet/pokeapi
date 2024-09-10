from unittest.mock import MagicMock
from pokeapi.services import pokemon_service

def get_pokemon_mock() -> dict:
    return {
        "id": 4,
        "name": "charmander",
        "height": 6,
        "weight": 85,
        "base_experience": 62,
        "is_default": True,
        "order": 5,
        "abilities": [],
        "forms": [],
        "game_indices": [],
        "held_items": [],
        "location_area_encounters": "https://pokeapi.co/api/v2/pokemon/4/encounters",
        "moves": [],
        "past_types": [],
        "sprites": {},
        "cries": {},
        "species": {},
        "stats": [],
        "types": []
    }

def test_get_pokemon() -> None:
    # Arrange
    pokemon_service.requests = MagicMock()
    pokemon_service.requests.get.return_value.json.return_value = get_pokemon_mock()
    service = pokemon_service.PokemonService()
    # Act
    result = service.get_pokemon("charmander")
    # Assert
    assert result is not None
    assert result.name == "charmander"
    assert result.id == 4

def test_get_pokemon_request_exception() -> None:
    # Arrange
    pokemon_service.requests = MagicMock()
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("An error")
    pokemon_service.requests.get.return_value = mock_response
    service = pokemon_service.PokemonService()
    # Act
    result = service.get_pokemon("charmander")
    # Assert
    assert result is None

def test_get_pokemon_json_exception() -> None:
    # Arrange
    pokemon_service.requests = MagicMock()
    mock_response = MagicMock()
    mock_response.json.side_effect = Exception()
    pokemon_service.requests.get.return_value = mock_response
    service = pokemon_service.PokemonService()
    # Act
    result = service.get_pokemon("charmander")
    # Assert
    assert result is None