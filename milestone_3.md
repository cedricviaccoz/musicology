# First results

This text contains a summary of the work done for Milestone 3. The notebooks "JSymbolic Feat. Analysis & Discussion.ipynb" and "First classification results.ipynb" should be read before approaching this text, they provide all the detailed results of the analysis made.

This milestone was made with two concurrent processes.
1. Analysis of the jSymbolic features (more details below) and was made in order to manually explore the features to see if they could provide some insight.
2. Classification using all the jSymbolic features to see how well it would perform without any feature engineering.


## Analysis
### JSymbolic features

The preliminary step consisted in feeding the MIDI database to the jSymbolic software (http://jmir.sourceforge.net/index_jSymbolic.html) in order to produce music theory-related features. This proved quite challenging as the software used a lot of memory and was slow to compute the features. In the end, the MIDIs had to be splitted by batch of 50 in order to be able to run jSymbolic. Finally, the features obtained were nicely all compiled into a file called "features.csv"

Some of the more general features were analyzed by hand in order to find their pertinence to the dataset and their potential concerning classification.
It was discovered that some of the analysed features did not show any relevant pattern if analyzed genre by genre, while others proved to be biased and ambigous by construction, providing little valid information. Some of them will certainly need to be recomputed in another way and others completely dropped. A more complete analysis can be found in the "JSymbolic Feat. Analysis & Discussion" notebook.

### Classification

The classification attempt proved unsuccessful, with at best 35% accuracy, and it was determined that the problem did not lie with the predictive models themselves, but was more likely linked with the data itself not providing enough information to discriminate between genres. A more detailed analysis of the classification can be found in the "First classification results" notebook.

This casts a little bit of doubt upon the original hypothesis of being able to tell the genre of a game by using its music, although it is still too soon to refute the research question. 

## Discussion
### Problems and difficulties

Through the feature analysis and the classification, some doubt about the quality of the MIDI files were raised, since they are user generated. One way to deal with this problem would be to use some jSymbolic features to find MIDIs that are obviously badly coded (such as those with 10'000 BPM tempo) and do a further cleaning step.

Concerning the features of jSymbolic, a more thorough analysis needs to be made to get rid of some obviously useless features, this will be done using the analysis of the "JSymbolic Feat. Analysis & Discussion" notebook. Another way of dealing with it could be to add some custom features, such as for example the compression ratio of midi files (to see the receptiveness) or using the results as key-finding algorithms as features.

Another problem could be linked to the fact that some midis were tied to several genres and it could impact the classification. If the other steps are not improving the results, this option could be explored, but it would require a lot of manual work in order to have something coherent.

### Next steps

Because of the result, it is evident that the use of all the features produced by jSymbolic at once is not effective.A more iterative approach should be considered for feature selection for the next step : In order to avoid bad features, jSymbolic features could be filtered using a more fine-grained study, a process akin to the one already done in this step. As there is no certainty such process would yield satisfactory results, new features could also be hand-crafted. Theses steps of adding feature and classifying could be repeated until a satisfying threshold would be attained. 




