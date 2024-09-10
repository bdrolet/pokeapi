from dataclasses import dataclass

@dataclass
class Generation:
    id: int
    name: str
    abilities: list
    names: list
    main_region: dict
    moves: list
    pokemon_species: list
    types: list
    version_groups: list