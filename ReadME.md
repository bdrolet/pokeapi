# Project Overview
This is a sample SDK for communicating with pokeapi. This is for demonstration purposes only.

pokeapi is a publically available api for requesting various facts about pokemon.

There are two endpoints that get called in this SDK...
* [https://pokeapi.co/docs/v2\#pokemon](https://pokeapi.co/docs/v2#pokemon)  
* [https://pokeapi.co/docs/v2\#generation](https://pokeapi.co/docs/v2#generation)
* Overview of PokeAPI and its endpoints (Pokémon and Generations).

# Building the project
Run: `make build`
# Installation
Run: `make install`

# Usage
  
* [https://pokeapi.co/docs/v2\#pokemon](https://pokeapi.co/docs/v2#pokemon)  
```python
>>> from pokeapi.generation import get_generation
>>> generation = get_generation("generation-i")
>>> generation.id
1
>>> generation.name
'generation-i'
>>> from pokeapi.pokemon import get_pokemon
>>> pokemon = get_pokemon("charmander")
>>> pokemon.id
4
>>> pokemon.name
'charmander'
>>> 
```
* [https://pokeapi.co/docs/v2\#generation](https://pokeapi.co/docs/v2#generation)
```python
>>> from pokeapi.generation import get_generation
>>> generation = get_generation("generation-i")
>>> generation.id
1
>>> generation.name
'generation-i'
>>> 
```

# Design Decisions
## Project Structure
The project has two main moduals:
* **models**: models representing the data returned
* **services**: contains the service class for communicating with pokeapi
```
models/
|  |-pokemon.py
|  |-generation.py
services/
|  |-pokemon_serivce.py
tests/
|  |-unit/
|  |-integration/ (integration tests)
|- pokemon.py (entry point)
|- generation.py (entry point)
 
```
## Entrypoint
`generation.py` contains a `get_generation` and
`pokemon.py` contains a `get_pokemon`

...see [ussage](#usage)

# Testing
* To run all tests, run `make test`
