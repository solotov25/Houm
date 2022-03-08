import requests

def min_max_weights():
    # Define variables to compare
    min = 10000000000000
    max = -1

    # Bring data of 151 first pokemon on API
    for pokemon in range(1,152):

        req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}/')
        query = req.json()['types']

        # Check if the pokemon type match with fighting 
        for pokemon_type in query:
            if pokemon_type['type']['name'] == 'fighting':
                if req.json()['weight'] < min:
                    min = req.json()['weight']
                if req.json()['weight'] > max:
                    max = req.json()['weight']

    return [max, min]