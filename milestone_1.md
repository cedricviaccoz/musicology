# Video game music: a genre study
## Research Question
The project will be done in the field of Ludomusicology, whose aim is to study video games music. The idea is to study the characteristics of video games music with respect to video games genres. More precisely, the goal is to isolate music features that allow to categorize a music piece as belonging to a certain video game genre.

This project's main challenge would be to prove or disprove the hypothesis that video games genres have distinctive musical features. This hypothesis sounds intuitively true to someone who has significant experience in playing video games, however no formal study on the matter seems to have been performed.
If the hypothesis is verified, it will be possible to understand which features are distinctive for a video game genre and interpret this result by using concepts from music theory and game design.
## Concepts and Data
The concrete focus of this project is understanding how the soundtrack of video games can help immerse the player into the game mechanics defined by the designers. For example, one might observe that racing game often use fast-paced compositions, which would obviously motivate players to adopt a nervous gameplay.

To do so, it is needed to identify and build abstract computational features that characterizes specific music accord to game genre. In order to define said features, many core musical elements can be used. Under the dimension of rhythm, the BPM, the time signature, as well as rhythmic patterns can help characterize songs into a particular game play. Under the dimension of pitch, chords, harmony, pitch class frequency and melodies are all elements that might be relevant and tied to a genre.

Fortunately, most game soundtracks are originally made in MIDI, or easily convertible into faithful MIDI files. Thus, individual pitches, notes duration and BPM can trivially be extracted. For the other more complex musical features, algorithms and computational tools can be used : pitch classes frequency can be obtained through histograms, slicing and pattern recognition can help identify melodies, and modular logic can identify chords.

What is needed to achieve this is a dataset of MIDI files where each file is categorized by video game genre. This dataset does not exist currently, but several sources that could easily be scrapped have been identified. The first one is [the video game music archive](https://vgmusic.com) that contains around 31’000 MIDI files. These MIDI files are hand-made, but are selected by the staff of the website, so in general they are good retranscription of the original music. Some cleaning has to be done, since the website also includes remixes and several submissions by song, but this can be taken care of in a latter step.

A problem with this website, is that it does not include any metadata regarding the video game, so no genre are directly included in the video game music archive. However, it is possible to cross-reference the game with other databases, such as [TheGamesDB.net](http://thegamesdb.net/) or [IGDB.com](https://www.igdb.com/) that provides quite complete video games metadatas and easily accessible APIs.
## Methods
There exists no current literature on video game music and video game genre that makes a computational analysis. The best way to tackle the problem would be to use an iterative approach : going back and forth from the conceptual background of video game genre, making hypothesis about what the music of such a genre should be like and then crafting features that would seem relevant to the genre. Statistical models will be used to see if the features allow distinction between different game genres and are indeed representative of a particular game genre. Eventually, this approach's end goal would be to find and interpret features that are related to different video game genres in order to gain a better understanding of the usage of music in video games.
## Literature
Studies on game music with respect to game genres have been already done in the past. These studies explores different game genres and find some general features of their music by analyzing several cases by “hand”, using a formal musicology point of view (Crathorne 2010; Summers 2011).

Studies on how to craft features for either MIDI files or audio files which are both informative and relevant for the genre classification task have been done in the past, though not in Ludomusicology, according to McKay and Fujinaga (2004, 2006).

The current literature seems to indicate that it is the first time a statistical-based study of the characteristic of music genres has been done in Ludomusicology. Furthermore, past studies usually focus on classification - meaning that they aim at successfully classifying music more than understanding the feature that allows the classification - while this project focuses on interpretation.

Extern help might be needed concerning computational tools, libraries or statistic models relevant to feature extraction in MIDI.

- Raphaël Barman (raphael.barman@epfl.ch)
- Hakim Invernizzi (hakim.invernizzi@epfl.ch)
- Cédric Viaccoz (cedric.viaccoz@epfl.ch)

# References
- Crathorne, P. J. (2010, March). Video game genres and their music. _University of Stellenbosch_. Retrieved from [http://scholar.sun.ac.za/handle/10019.1/4355](http://scholar.sun.ac.za/handle/10019.1/4355)
- Summers, T. (2011, February). Playing the Tune: Video Game Music, Gamers, and Genre. _Universität Bayreuth_. Retrived from [https://epub.uni-bayreuth.de/322/](https://epub.uni-bayreuth.de/322/)
- McKay, C.; Fujinaga I. (2004). AUTOMATIC GENRE CLASSIFICATION USING LARGE HIGH-LEVEL MUSICAL FEATURE SETS. _McGill University_. Retrieved from [http://www.music.mcgill.ca/~ich/research/ismir2004/McKay_Fujinaga_ISMIR_2004.pdf](http://www.music.mcgill.ca/~ich/research/ismir2004/McKay_Fujinaga_ISMIR_2004.pdf)
- McKay, C.; Fujinaga I. (2006).jSymbolic: A Feature Extractor for MIDI Files. _McGill University_. Retrieved from [http://jmir.sourceforge.net/publications/ICMC_2006_jSymbolic.pdf](http://jmir.sourceforge.net/publications/ICMC_2006_jSymbolic.pdf)

