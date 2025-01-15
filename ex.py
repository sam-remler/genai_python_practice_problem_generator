messed_pokemon = 'BulbAsaur-ChaRMAndeR-pikaCHU-chariZard-SQuirtlE'

pokelist = messed_pokemon.split("-")
pokedex = []

for pokemon in pokelist:
    if pokemon.capitalize() != 'Charizard':
        pokedex.append(pokemon.capitalize())
