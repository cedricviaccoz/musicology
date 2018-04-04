import os
from itertools import groupby
import json
from requests import get
from collections import OrderedDict
import xmltodict
from fuzzywuzzy import process

def give_choices(target, candidates, limit=5):
    choices = process.extract(target, candidates, limit=limit)
    print('Choices for', target)
    for idx, choice in enumerate(choices):
        print("%d: %s"%(idx, choice))
    idx = int(input("Enter a number between 0 and %d, if the name is not present, enter -1: "%(len(choices)-1)))
    if idx >= 0:
        return choices[idx][0]
    else:
        return None


def get_consoles_mapping(midi_db):
    if os.path.isfile('tgdb_consoles_mapping.json'):
        return json.load(open('tgdb_consoles_mapping.json'))
    consoles = set()
    for midi in midi_db:
        consoles.add(midi['console'])
    
    # If the list of consoles of tgdb is not present, fetch it
    if not os.path.isfile('tgdb_consoles.json'):
        res = get('http://thegamesdb.net/api/GetPlatformsList.php')
        data = xmltodict.parse(res.text)['Data']['Platforms']['Platform']
        data = [console['name'] for console in data]
        with open('tgdb_consoles.json', 'w') as outfile:
            json.dump(data, outfile)
    
    tgdb_consoles  = json.load(open('tgdb_consoles.json'))
    
    tgdb_consoles_mapping = {}
    
    for console in consoles:
        match = process.extractOne(console, tgdb_consoles)
        if match[1] >= 91:
            print("%s -> %s"%(console,match[0]))
            tgdb_consoles_mapping[console] = match[0]
        else:
            idx = give_choices(console, tgdb_consoles)
            if not idx:
                tgdb_consoles_mapping[console] = input("Enter manually the name: ")
            else: 
                tgdb_consoles_mapping[console] = idx
            print("%s -> %s"%(console,tgdb_consoles_mapping[console]))


    with open('tgdb_consoles_mapping.json', 'w') as outfile:
        json.dump(tgdb_consoles_mapping, outfile)

    return tgdb_consoles_mapping

def match_game(game, exact=True, platform=True, interactive=False):

    game_name = game[1]
    console_id = game[0]
    name = 'exactname' if exact else 'name'
    platform_string = '&platform=%s'%console_id if platform else ''
    res = get('http://thegamesdb.net/api/GetGame.php?%s=%s%s'
                  %(name, game_name, platform_string))
    if res.status_code != 200:
        print("Bad status code")
        return None
    data = xmltodict.parse(res.text)
    if 'Data' in data:
        data = data['Data']
    else:
        print("Problem with data...", data)
        print(console_id)
        return None

    if 'Game' in data:
        data = data['Game']
        if isinstance(data, OrderedDict):
            print("%s -> %s"%(game_name,data['GameTitle']))
            return data
        names = {game['GameTitle']: idx for idx, game in enumerate(data)}

        match = process.extractOne(game_name, names.keys())
        if match[1] >= 95:
            print("%s -> %s"%(game_name,match[0]))
            return data[names[match[0]]]
        elif interactive:
            idx = give_choices(game_name, list(names.keys()))
            if idx:
                print("%s -> %s"%(game_name,data[names[idx]]['GameTitle']))
                return data[names[idx]]
    if not exact and not platform and interactive:
        game_id =  int(input("Enter the game id from tgdb or -1 if not present: "))
        if game_id < 0:
            return None
        res = get('http://thegamesdb.net/api/GetGame.php?id=%d'%game_id)
        if res.status_code != 200:
            print("Bad status code")
            return None
        data = xmltodict.parse(res.text)
        if 'Data' in data:
            data = data['Data']
        else:
            print("Problem with data...", data)
            return None
        if 'Game' in data:
            data = data['Game']
            if isinstance(data, OrderedDict):
                print("%s -> %s"%(game_name,data['GameTitle']))
                return data
            else:
                print("Data is not a single game")
                return None




    return None


# Toggle to treat previously not found games
find_not_founds = True
resume_discard = True

if find_not_founds:
    games = set([(x[0], x[1]) for x in json.load(open('not_found_games.json'))])
    with open('game_data_raw_appendix.json', 'r', encoding = 'utf-8') as infile:
        already_found = set([(x[0][0], x[0][1]) for x in json.load(infile)])
        games.difference_update(already_found)
    if resume_discard:
        with open('not_found_games_appendix.json', 'r', encoding = 'utf-8') as infile:
            already_discarded = set([(x[0],x[1]) for x in json.load(infile)])
            games.difference_update(already_discarded)

else:
    midi_db = json.load(open('midi_db.json'))
    
    consoles_mapping = get_consoles_mapping(midi_db)
    
    games = set()
    for midi in midi_db:
        games.add((consoles_mapping[midi['console']], midi['game']))

num_games = len(games)

game_data = []
not_found_games = set()

for idx, game in enumerate(games):
    print('%d/%d:'%(idx+1, num_games), game)
    for bool1 in (True, False):
        for bool2 in (True, False):
            res = match_game(game, bool1, bool2, find_not_founds)
            if res:
                break
        else:
            continue
        break

    if res:
        game_data.append((game, res))
        if find_not_founds:
            with open('game_data_raw_appendix.json', 'w', encoding = 'utf-8') as outfile:
                json.dump(game_data, outfile)
    else:
        not_found_games.add(game)
        if find_not_founds:
            with open('not_found_games_appendix.json', 'w', encoding = 'utf-8') as outfile:
                json.dump(list(not_found_games), outfile)
        print("Not found!")

if not find_not_founds:
    with open('game_data_raw.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(game_data, outfile)
    with open('not_found_games.json', 'w', encoding = 'utf-8') as outfile:
        json.dump(list(not_found_games), outfile)
print(len(not_found_games))

