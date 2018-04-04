import json
import hashlib
import os
from shutil import copyfile

data = json.load(open('midis.json'))

orig_path = "full/"

midis = []

for midi in data:
    orig_filename = hashlib.sha1(midi['file_urls'][0].encode('utf-8')).hexdigest()+".mid"

    target_path = 'midis/' + midi['file_path']
    target_filename = midi['file_urls'][0].rsplit('/', 1)[-1]

    if not os.path.exists(target_path):
        os.makedirs(target_path)

    copyfile(orig_path+orig_filename, target_path + "/" +target_filename)
