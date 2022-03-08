import requests

def count_pokemon_conditions():
    req = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=1126')
    query = req.json()['results']

    is_valid = 0
    for element in query:
        # Boolean string has 'at' inside
        at_in_string = 'at' in element['name']
        # Boolean string has 2 a'
        double_a_string = element['name'].count('a') == 2

        if at_in_string and double_a_string: 
            is_valid +=1 

    return is_valid