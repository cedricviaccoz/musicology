# Video game music: a genre study
## Research Question
The project will be done in the field of Ludomusicology, which aims at studying video games music. The idea is to study the characteristics of video games music with respect to video games genres. More precisely, the goal is to isolate music features that allow to categorize a music piece as belonging to a certain video game genre.

This project is interesting because it could allow to prove or disprove the hypothesis that video games genres have distinctive musical features. This hypothesis sounds to be intuitively true to someone who has significant experience in playing video games, however no formal study on the matter seems to have been performed.
If the hypothesis verified, then it will be possible to understand which features are distinctive for a video game genre and interpret this result by using concepts from music theory and game design.
## Concepts and Data
The concrete focus of this project is understanding how the soundtrack of video games can help immerse the player into the game mechanics defined by the designers. For example, we might observe that racing game often use fast-paced compositions, which would obviously motivate players to display a nervous gameplay.

To do so, we are going to identify and build abstract computational features that characterizes specific music accord to game genre. In order to define said features, many core musical elements can be used. Under the dimension of rhythm, the BPM, the time signature, as well as rhythmic patterns can help characterize songs into a particular game play. Under the dimension of pitch, pitch class frequency, chords, harmony and melodies are all elements that might be relevant and tied to a genre.

Fortunately for us, most game soundtracks are originally made in MIDI, or easily convertible into faithful MIDI files. Thus, individual pitches, notes duration and BPM can trivially be extracted. For the other more complex musical features, algorithms and computational tools can be used : pitch classes frequency can be obtained through histograms, slicing and pattern recognition can help identify melodies,...

What is needed to achieve this is a dataset of MIDI files where each file is categorized by video game genre. This dataset does not exist currently, but several sources that could easily be scrapped have been identified. The first one is [the video game music archive](https://vgmusic.com) that contains around 31’000 MIDI files. These MIDI files are hand-made, but are selected by the staff of the website, so in general they are good retranscription of the original music. Some cleaning has to be done, since the website also includes remixes and several submissions by song, but this can be taken care of in a latter step.

A problem with this website, is that it does not include any metadata regarding the video game, so no genre are directly included in the video game music archive. However, it is possible to cross-reference the game with other databases, such as [TheGamesDB.net](http://thegamesdb.net/) or [IGDB.com](https://www.igdb.com/) that provides quite complete video games metadata and easily accessible APIs.
## Methods
There exists no current literature on video game music and video game genre that makes a computational analysis. We will use an iterative approach, going back and forth from the conceptual background of video game genre, making hypothesis about what the music of such a genre should be like and we will be crafting features that would seem relevant to the genre. Then we will use statistical models to see if the features allow distinction between different game genres and are indeed representative of a particular game genre. This approach will allow us to find and interpret the features that are related to different video game genres and have a better understanding of the usage of music in video games.
## Literature
Studies on game music with respect to game genres have been already done in the past. These studies explores different game genres and find some general features of their music by analyzing several cases by “hand”, using a formal musicology point of view. See:
- [Crathorne 2010](http://scholar.sun.ac.za/handle/10019.1/4355)
- [Summers 2011](https://epub.uni-bayreuth.de/322/)

Studies on how to craft features for either MIDI files or audio files which are both informative and relevant for the genre classification task have been done in the past, though not in Ludomusicology.
See:
- [McKay and Fujinaga 2004](http://www.music.mcgill.ca/~ich/research/ismir2004/McKay_Fujinaga_ISMIR_2004.pdf)
- [McKay and Fujinaga 2006](http://jmir.sourceforge.net/publications/ICMC_2006_jSymbolic.pdf)

As far as we know, this it the first time that a statistical-based study of the characteristic of music genres has been done in Ludomusicology. Furthermore, past studies usually focus on classification - meaning that they aim at successfully classifying music more than understanding the feature that allows the classification - while our project focuses on interpretation.

Help might be needed concerning computational tools, libraries or statistic models relevant to feature extraction in MIDI.

- Raphaël Barman (raphael.barman@epfl.ch)
- Hakim Invernizzi (hakim.invernizzi@epfl.ch)
- Cédric Viaccoz (cedric.viaccoz@epfl.ch)

