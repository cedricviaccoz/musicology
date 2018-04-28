# Video Game Music : A study of genre
Repository for the DH-401 course project.

## Organisation of the repository :

```
.
+-- _dataset
|  +-- _parsing
|  +-- _scraper
|  |  +-- _vgmusic
|  |  +-- midis.json
|  +-- Data Exploration.ipynb
|  +-- Midi Exploration.ipynb
|  +-- README.md
+-- milestone_1.md
+-- milestone_2.md
+-- README.md
```

The main folder of the project is currently the "dataset" one, which holds all the script for the data scrapping, and notebooks for the data analysis and exploration. On the structure above, folder are preceded by an underscore, in opposition to the normal files which are preceded by nothing particular. 

The first folder "parsing" contains all the raw JSONs produced by the scraping, as well as 3 python script used to parse the raw JSONs into preprocessed JSONs needed for cross-referencing, that are also present within this folder.

The second one "scraper", contains a subfolder "vgmusic" which holds all the relevant scraping scripts, and the file midis.json, which holds all metadata of the midis retrieved from the video game music archive.

Then, the "dataset" folder contains a first jupyter notebook  named"Data Exploration.ipynb" that was used to filter unnecessary MIDI files and construct some basic statistics on the dataset. The second jupyter notebook was some experimentation of the 3rd week tutorial notebook of Digital Musicology course on 2 MIDIs from the dataset. The "README.md" in this folder lists all dependencies needed to run the scraper.

On the same level as this README, are two markdown text, the first indexed being the project proposal of the first milestone explaining the aim of the project, while the second summarize the whole data gathering and preprocessing as well as some basic statistics on the dataset. 
