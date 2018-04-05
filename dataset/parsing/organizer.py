import json
import hashlib
import os
from shutil import copyfile

data = json.load(open('midis.json'))

midis_path = "midis/full/"

midis = []

for midi in data:
    path = hashlib.sha1(midi['file_urls'][0].encode('utf-8')).hexdigest()+".mid"


    midi_struct = {
        'brand': midi['brand'],
        'console': midi['console'],
        'game': midi['game'],
        'title': midi['title'],
        'path': midis_path + path
    }
    midis.append(midi_struct)

with open('midi_db.json', 'w') as outfile:
    json.dump(midis, outfile)
