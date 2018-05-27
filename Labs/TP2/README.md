# [SD-TSIA214] TP 2 - Sentiment Analysis

- Davide GALLITELLI
- Carlotta CASTELLUCCIO

### Question 1 - Scikit-Learn compare

Accuracy obtained with **our custom classifier**:
![My_accuracy.png](My_accuracy.png)

Accuracy obtained with **Scikit MultinomialNB classifier**:
![scikit_accuracy.png](scikit_accuracy.png)

Our custom classifier has better performances, although slower in running. Standard deviation is generally better too.

### Question 2 - Testing another classifier

Accuracy obtained with **Scikit Logistic Regression classifier**:
![lr_accuracy.png](lr_accuracy.png)

### Question 3 - NLTK Stemming

![stem_accuracy.png](stem_accuracy.png)

Stemming the words does not seem to improve the accuracy of our classifier, just speeding it up a little bit since there are less words to check in the vocabulary.

### Question 4 - Stemming + POS_TAG

![stem2_accuracy.png](stem2_accuracy.png)
