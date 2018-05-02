# First results

TODO seperations + text

- bla bla about the different files + logic of not putting everything in the same document
- Both analysis done in parallel, but in ML4 will converge
- Explain in a few lines what has been done and that the results were not very good
- Explain that prior assumption = challenged at first glance, seems not able to classify music by video game genres
- Problems and Difficulties, why? How to solve?
  - Bad midis, because of users (extreme tempo) -> solution ? See proportion, if not too much, remove, but need to have good understanding and control of features.
  - Bad features, for our purpose from JSymbolic? Supported by results? Some features seems useless (e.g. Violin stuff), solution = make better sort of features using Cedric's analysis, maybe create new features
  - Several genres by midi, solution = do a closer analysis of multi-genre games using random sampling, own knowledge and several sources
- Next steps
  - Select feature by feature, incremental process, feature verified by "hand"
  - Implement different solutions proposed previously
  - See if it improves the results


This text contains a summary of the work done for Milestone 3. The notebooks "JSymbolic Feat. Analysis & Discussion.ipynb" and "First classification results.ipynb" should be read before approaching this text. 


This milestone entailed a preliminary step followed by the main research .

The preliminary step consisted in feeding our MIDI database to the Jsymbolic software (http://jmir.sourceforge.net/index_jSymbolic.html) in order to produce music theory-related features. 
The features obtained with this procedures are stored in features.csv.

The main research comprised two main activities: on one side, the first attempt at classifing video game music by genre; on the other side, the analysis of the features used for classification in order to extract meaningful insight.

The classification attemp proved unsuccessful, and it was determined that the problem didn't lie with the predictive models itself. The hypothesis that the problem lied within the data itself was therefore formulated. The analysis of the features provided some facts that also hint towards that direction. Namely, some of the analysed features didn't show any relevant pattern if analyzed genre by genre, while others proved to be biased and ambigous by construction, providing little valid information. These observations called into question both the quality of the original MIDI dataset and the pertinence of the features produced by JSymbolic. They also cast doubt upon the original hypothesis of being able to tell the genre of a game by using its music, altough it is still too soon to give up. 

There are some approaches that could potentially solve our problem with the crafting of informative features. 

Concerning the quality of our dataset, the problem most likely lies in the fact that it is a dataset created by users and therefore there's no control over the correctness of the MIDI's content. A first thing to do would be discard all those MIDIs who contain values that are outliers or simply totally unresonable. This would be a form of cleaning which could improve the feature extraction done by Jsymbolic.
[someone add more because I didn't fully understand the solution]

Concerning the crafting of features, it is evident that using those produced by Jsymbolic by itself isn't effective. This makes sense because the goal of these feature wasn't to do classification, and therefore we need to try adapting them to our purpose. A solution could be selecting a few among them that look promising and trying to manipulate them to create custom features. This would be done in a incremental way, i.e. by producing a feature, seeing its impact on the classification task, then adding another feature and see if there's an improvement. This approach implies fine-grained study of the existing JSymbolic features.






