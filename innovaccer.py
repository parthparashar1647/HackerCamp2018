import dedupe                               # For deduplication
import pandas as pd                         # For Data Management and Representation

# Loading the Dataset
df = pd.read_csv('sample_input.csv')
df.head()

df['ID'] = range(len(df.index))

Train = df.to_dict('ID')
print(Train)

training_file = 'csv_example_training.json'

    # ## Training

    # Define the fields dedupe will pay attention to
fields = [
            {'field' : 'ln', 'type': 'String'},
            {'field' : 'dob', 'type': 'String'},
            {'field' : 'gn', 'type': 'String'},
            {'field' : 'fn', 'type': 'String'},
        ]

    # Create a new deduper object and pass our data model to it.
deduper = dedupe.Dedupe(fields)

    # To train dedupe, we feed it a sample of records.
deduper.sample(Train, 15000)
    # ## Active learning
    # Dedupe will find the next pair of records
    # it is least certain about and ask you to label them as duplicates
    # or not.
    # use 'y', 'n' and 'u' keys to flag duplicates
    # press 'f' when you are finished
print('starting active labeling...')
dedupe.consoleLabel(deduper)

    # Using the examples we just labeled, train the deduper and learn
    # blocking predicates
deduper.train()

    # When finished, save our training to disk
with open(training_file, 'w') as tf:
        deduper.writeTraining(tf)

    # Save our weights and predicates to disk.  If the settings file
    # exists, we will skip all the training and learning next time we run
    # this file.
with open(settings_file, 'wb') as sf:
    deduper.writeSettings(sf)
threshold = deduper.threshold(Train, recall_weight=1)
clustered_dupes = deduper.match(Train, threshold)
for (cluster_id, cluster) in enumerate(clustered_dupes):
    id_set, scores = cluster
    cluster_d = [Train[c] for c in id_set]
list1 = [] # list1 contains all the entries for duplicate record clusters for ex. (66, 67, 68, 69, 70, 71, 72, 73, 74)
list2 = [] # list2 contains the first entry of the duplicate record for each cluster we have found for ex.(66)
newlist = [] # newlist contains the entries except list2 which is for ex. (67, 68, 69, 70, 71, 72, 73, 74)
finallist = [] # finallist contains all the indexes except those present in newlist
for (cluster_id, cluster) in enumerate(clustered_dupes):
    list2.append(cluster[0][0])
    for i in cluster[0]:
        list1.append(i)

newlist = list(set(list1) - set(list2))

for i in range(df.shape[0]):
    finallist.append(i)

finallist = list(set(finallist) - set(newlist))
FinalDF = pd.DataFrame(columns=['ln','dob','gn','fn'])
for i in finallist:
    FinalDF = FinalDF.append(df.iloc[i])

FinalDF = FinalDF.drop(['ID'], axis=1)
FinalDF.to_csv('sample_output.csv', index=False)


##Now using trained settings on the test data

test_df = pd.read_csv('test.csv')
#this csv file contains all possible duplicates of Vldamir Frometa given in the question
test_df['ID'] = range(len(test_df.index))
Test = test_df.to_dict('ID')
clustered_dupes = deduper.match(Test, threshold)
for (cluster_id, cluster) in enumerate(clustered_dupes):
    id_set, scores = cluster
    cluster_d = [Test[c] for c in id_set]
list1 = [] # list1 contains all the entries for duplicate record clusters for ex. (66, 67, 68, 69, 70, 71, 72, 73, 74)
list2 = [] # list2 contains the first entry of the duplicate record for each cluster we have found for ex.(66)
newlist = [] # newlist contains the entries except list2 which is for ex. (67, 68, 69, 70, 71, 72, 73, 74)
finallist = [] # finallist contains all the indexes except those present in newlist
for (cluster_id, cluster) in enumerate(clustered_dupes):
    list2.append(cluster[0][0])
    for i in cluster[0]:
        list1.append(i)

newlist = list(set(list1) - set(list2))

for i in range(test_df.shape[0]):
    finallist.append(i)

finallist = list(set(finallist) - set(newlist))
Final_testdf = pd.DataFrame(columns=['ln','dob','gn','fn'])
for i in finallist:
    Final_testdf = Final_testdf.append(test_df.iloc[i])

Final_testdf = Final_testdf.drop(['ID'], axis=1)

Final_testdf.to_csv('resolved_test.csv', index=False)
#finally only one entry Vldamir Formeta




