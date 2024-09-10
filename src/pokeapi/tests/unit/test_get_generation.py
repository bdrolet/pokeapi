from unittest.mock import MagicMock
from pokeapi.services import pokemon_service

def get_generation_mock() -> dict:
    return {
        "id": 4,
        "name": "generation-i",
        "abilities": [],
        "main_region": {},
        "moves": [],
        "pokemon_species": [
            {
                "name": "charmander",
                "url": "https://pokeapi.co/api/v2/pokemon-species/4/"
            }
        ],
        "types": [],
        "version_groups": []
    }

def test_get_generation() -> None:
    # Arrange
    pokemon_service.requests = MagicMock()
    pokemon_service.requests.get.return_value.json.return_value = get_generation_mock()
    service = pokemon_service.PokemonService()
    # Act
    result = service.get_generation("generation-i")
    
    # Assert
    assert result is not None
    assert result.name == "generation-i"
    assert result.id == 4

def test_get_generation_request_exception() -> None:
    # Arrange
    pokemon_service.requests = MagicMock()
    mock_response = MagicMock()
    mock_response.raise_for_status.side_effect = Exception("An error")
    pokemon_service.requests.get.return_value = mock_response
    service = pokemon_service.PokemonService()
    # Act
    result = service.get_generation("generation-i")
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
    result = service.get_generation("generation-i")
    # Assert
    assert result is None