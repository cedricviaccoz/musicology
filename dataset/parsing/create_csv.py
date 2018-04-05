import json
import pandas as pd

game_data = json.load(open('game_data_raw.json', encoding='utf-8'))
game_data.extend(json.load(open('game_data_raw_appendix.json', encoding='utf-8')))
midi_db = json.load(open('midi_db.json', encoding='utf-8'))
consoles_mapping = json.load(open('tgdb_consoles_mapping.json', encoding='utf-8'))

game_data = {(x[0][0], x[0][1]): x[1] for x in game_data}

data = []

for midi in midi_db:
    midi_data = {'brand': midi['brand'],
                 'console': midi['console'],
                 'game': midi['game'],
                 'title': midi['title'],
                 'file_name': midi['path'].split('/')[-1]
                }
    key = (consoles_mapping[midi['console']], midi['game'])
    if key in game_data:
        for info in ['Developer', 'ESRB', 'GameTitle', 'Overview', 'Platform', 'Players', 'Publisher', 'Rating', 'ReleaseDate', 'id']:
            midi_data['tgdb_%s'%(info.lower())] = game_data[key].get(info)
        if 'Genres' in game_data[key]:
            genres = game_data[key]['Genres'].get('genre')
        if isinstance(genres, str):
            genres = [genres]
        midi_data['tgdb_genres'] = genres
    data.append(midi_data)
df = pd.DataFrame(data)
df.tgdb_releasedate = pd.to_datetime(df.tgdb_releasedate)
df = df[['brand', 'console', 'game', 'title', 'file_name', 'tgdb_genres', 'tgdb_id', 'tgdb_developer', 'tgdb_publisher', 'tgdb_platform', 'tgdb_gametitle', 'tgdb_releasedate', 'tgdb_players', 'tgdb_rating', 'tgdb_esrb', 'tgdb_overview']]

df.to_csv('midi_dataframe.csv', index=False)

data = []

for midi in midi_db:
    midi_data = {'brand': midi['brand'],
                 'console': midi['console'],
                 'game': midi['game'],
                 'title': midi['title'],
                 'file_name': midi['path'].split('/')[-1]
                }
    key = (consoles_mapping[midi['console']], midi['game'])
    if key in game_data:
        for info in ['Developer', 'ESRB', 'GameTitle', 'Overview', 'Platform', 'Players', 'Publisher', 'Rating', 'ReleaseDate', 'id']:
            midi_data['tgdb_%s'%(info.lower())] = game_data[key].get(info)
        if 'Genres' in game_data[key]:
            genres = game_data[key]['Genres'].get('genre')
            if isinstance(genres, str):
                midi_data['tgdb_genres'] = genres
                data.append(midi_data)
            else:
                for genre in genres:
                    midi_data = midi_data.copy()
                    midi_data['tgdb_genres'] = genre
                    data.append(midi_data)
df = pd.DataFrame(data)
df.tgdb_releasedate = pd.to_datetime(df.tgdb_releasedate)
df = df[['brand', 'console', 'game', 'title', 'file_name', 'tgdb_genres', 'tgdb_id', 'tgdb_developer', 'tgdb_publisher', 'tgdb_platform', 'tgdb_gametitle', 'tgdb_releasedate', 'tgdb_players', 'tgdb_rating', 'tgdb_esrb', 'tgdb_overview']]

df.to_csv('midi_dataframe_genres.csv', index=False)
