# Dataset Construction

## Data Gathering 
The core of the dataset consists of 31658 MIDI files, fetched from the the [Video Game Music Archive(VGMA)](https://vgmusic.com), an online platform whose aim is to build the most complete archive of user-contributed video game music MIDIs. The songs on this website are organized hierachically in three levels, the first being the video game console, the second the game, and finally the song's title. Each file also holds on the website as metadata its size in Bytes, the name of the user who sequenced it, and optionally, a list of comments.

However, one crucial metadata was missing for the purpose of this research: the game genre. To associate each MIDI file to a genre, cross-referencing was done using another resource: [TheGamesDB.net (TGDB)](http://thegamesdb.net/). [IGDB.com](https://www.igdb.com/) was also considered at one point, but considering its API was not free, this option was quickly dropped.

Fetching all the necesserary data was mostly automatised using python scripts running the [scrappy library](https://scrapy.org). 

The matching was done using both the information of the console from the VGMA and the game title, the treshold for the game title was set quite high to avoid bad matching. Using this method, out of the 3918 games that all the MIDI files belongs to, 690 could not be automatically referenced. Those unmatched games were assigned manually to a game from TGDB and out of those 690, only 152 were not matched at all (mainly because they either referenced games that did not exist on TGDB or because they referenced several games, because there are some medleys on VGMA).

## Preprocessing 
Except the actual MIDI files, raw data scraped from both sources were stored in JSON file, and put in common in one CSV file which serve as the entry point for the data analysis, containing the following fields (all fields containing the prefix "tgdb" are informations obtained on TheVideoGamesDB.net) : 
* _brand_: The video game industry which has produced the console.
* _console_: The game system on which the game was edited.
* _title_: Title of the video game song
* _game_: The name of the video game on which the song can be heard.
* _file\_name_: The name of the MIDI file corresponding to the song.
* _tgdb\_genres_: The genre(s) associated to the game.
* _tgdb\_id_: Internal unique ID used by TheGamesDB.net to identifiy the game.
* _tgdb\_developer_: The game company which developped the game.
* _tgdb\_publisher_: The company which published the game.
* _tgdb\_gametitle_: Title of the game.
* _tgdb\_releasedate_: Date on which the game was released.
* _tgdb\_players_: Maximum number of player by which the game can be played.
* _tgdb\_rating_: Average of all user-submitted rating out of ten on the game.
* _tgdb\_esrb_: Age restriction rating given to the game by the [ESRB](http://www.esrb.org)(Entertainment Software Rating Board)
* _tgdb\_overview_: Short summary of the game's content.

Although only the fields _tgdb\_genres_ and _file\_name_ (which is a reference to the actual MIDI file) are of in interest for the current research question, all the other fields might also be interesting for future research, to find not only identify musical feature relevant by genre, but by publisher, or consoles.

Before being ready to use, the data needed some cleaning. The first step consisted of removing pure duplicates. Fortunately, it was only the case for two MIDI files. In the second step, all MIDIs whose games had not any genre declared were removed, thus shortening the dataset by 436 files. One side effect of the user submitted policy of the video game music archive, was that a lot of MIDI were remixes or simplified piano version of the songs. Since versions as close as to the original are wanted to do an ideally unbiased feature analysis, all thos alternative versions were removed,ligthening the dataset from 2732 MIDIs. Finally, another side-effect inherent of the plateform's policy was all songs which were submitted by different users. The webplatform would denote all those "duplicates" with (1), (2),... in the title. This was definitively the most consequence reduction of the dataset, as 6358 files were concerned.

All this cleaning reducted the original number of 31658 files to 22179. 

## Basic Statistics
Since this research will focus on video game genres, already some basic statistics were computed. 19 genres were identified in total, however, only 10 represents indivuadally at least 3% of the dataset, and 6 represent at least 9%. Below is a table holding the percentage on how each category is represented within the dataset : 

| Category | % |
| -------- | -------- |
| Action | 44.93 |
| Role-Playing | 33.84 |
| Platform | 27.28 |
| Adventure | 26.16 |
| Shooter | 9.39 |
| Figthing | 7.61 |
| Puzzle | 7.20 |
| Sports | 5.03 |
| Strategy | 4.39 |
| Racing | 3.68 |
| Stealth | 0.83 |
| Life Simulation | 0.79 |
| Horror | 0.62 |
| Music | 0.40 |
| Construction and Management Simulation | 0.35 |
| Sandbox | 0.36 |
| MMO | 0.35 |
| Flight Simulator | 0.26 |
| Vehicle Simulation | <0.01 |

Games can have multiples genres (like Action-Adventure, MMO-Figthing, and others) thus such games were counted in all individual categories. At this point nothing can really be inferred about the research question, except that most of the database consists of the 4 first genres listed on the table above. 

#Subsequent steps

