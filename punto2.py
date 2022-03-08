import requests

def species_to_procreate(pokemon_to_search):

    # Look up for species of pokemon 
    req_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_to_search}/')
    url_query = req_pokemon.json()['species']['url']

    # Look what is the egg group that belong the pokemon
    req_egg = requests.get(url_query)
    url_query = req_egg.json()['egg_groups']

    eggs = []

    for i in url_query:
        eggs.append(i['name'])

    # Create a set to store species 
    species = set()

    for pokemon_species in eggs:
        req = requests.get(f'https://pokeapi.co/api/v2/egg-group/{pokemon_species}/')
        query = req.json()['pokemon_species']

        # Store name in a set
        for species_name in query:
            species.add(species_name['name'])

    # Remove pokemon from set to avoid duplicates
    species.remove(pokemon_to_search)

    return len(species)