from dataclasses import dataclass

@dataclass
class Pokemon:
    id: int
    name: str
    height: int
    weight: int
    base_experience: int
    is_default: bool
    order: int
    weight: int
    abilities: list # PokemonAbility
    forms: list # PokemonForm
    game_indices: list # PokemonGameIndex
    held_items: list # PokemonHeldItem
    location_area_encounters: str
    moves: list # PokemonMove
    past_types: list # PokemonType
    sprites: dict # PokemonSprites
    cries: dict # PokemonCries
    species: dict # PokemonSpecies
    stats: list # PokemonStat
    types: list

# class PokemonAbility:
#     ability: dict # Ability
#     is_hidden: bool
#     slot: int

# @dataclass
# class PokemonType:
#     slot: int
#     type: dict

# @dataclass
# class PokemonFormType:
#     slot: int
#     type: dict # Type
# @dataclass
# class PokemonTypePast:
#     generation: dict #Generation
#     types: list # Type

# @dataclass
# class PokemonHeldItem:
#     item: dict #Item
#     version_details: list #Version

# @dataclass
# class PokemonHeldItemVersion:
#     version: dict # Version
#     rarity: int

# @dataclass
# class PokemonMove:
#     move: dict # Move
#     version_group_details: list # PokemonMoveVersion

# @dataclass
# class PokemonMoveVersion:
#     move_learn_method: dict #MoveLearnMethod
#     version_group: dict #VersionGroup
#     level_learned_at: int

# @dataclass
# class PokemonStat:
#     stat: dict # Stat  
#     effort: int
#     base_stat: int

# @dataclass
# class PokemonSprites:
#     front_default: str
#     front_shiny: str
#     front_female: str
#     front_shiny_female: str
#     back_default: str
#     back_shiny: str
#     back_feamale: str
