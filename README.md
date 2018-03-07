# HackerCamp2018


Problem Statement:
To train a model to identify unique patients in the sample dataset.
Sample dataset is given which is not labelled.

Scenario given:
Variation in names leads to difficulty in identifying a unique person and hence deduplication
of records is an unsolved challenge. The problem becomes more complicated in cases where
data is coming from multiple sources. Following variations are same as Vladimir Frometa:
Vladimir Antonio Frometa Garo ,
Vladimir A Frometa Garo ,
Vladimir Frometa ,
Vladimir Frometa G ,
Vladimir A Frometa ,
Vladimir A Frometa G .

To solve :
Used python 3.6.
Used python library dedupe which used method of active learning and then divide the data into cluster to get unique entries.
The code is in ``` innovaccer.py ``` and the input to train the model is ``` sample_input.csv ``` .
The output is stored in ``` sample_output.csv ``` .
For testing the model used ``` test.csv ``` .
The output of the testing is ``` resolved_test.csv ``` .
#### Steps to run the code
1. install pandas : ``` pip install pandas ```
2. install numpy required by dedupe: ``` pip install "numpy>=1.9" ```
3. install dedupe : ``` pip install dedupe ```
4. open terminal and type : ``` python innovaccer.py ```

The reason for using dedupe and approach used by dedupe is discussed in the Approach.pptx.


Kindly copy all contents in one folder to avoid errors
