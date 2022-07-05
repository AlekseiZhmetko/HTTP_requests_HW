import requests

heroes_pick = ['Hulk', 'Captain America', 'Thanos']
def most_int_hero(list):
    r = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    heroes_int_list = {}
    for hero in r.json():
        if hero['name'] in heroes_pick:
            heroes_int_list[hero['name']] = hero['powerstats']['intelligence']
    print(max(heroes_int_list))

most_int_hero(heroes_pick)
