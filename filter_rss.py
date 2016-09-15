#!/usr/bin/python3

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from nltk.stem import WordNetLemmatizer


def lemmatize_sentence(sentence, lemmatizer):
    return " ".join([lemmatizer(a) for a in sentence.split()])

headlines = ["a duck metaphorically ate the president of GM",
             "Dogs constantly chase cats",
             "ducks are terrible",
             "Headline, Headline, The world is ending"]

lemmatizer = WordNetLemmatizer()
lem = lemmatizer.lemmatize

test_headlines = [lemmatize_sentence(a, lem) for a in  ["duck are evil", "ducks are evil",  "They ate my family"]]

vectorizer = TfidfVectorizer(stop_words="english", use_idf=True)
counts = vectorizer.fit_transform(headlines)
answers = np.array([1, 1, 0, 0])
clf = MultinomialNB()
clf.fit(counts, answers) 

test = vectorizer.transform(test_headlines)
prediction  = clf.predict(test)

print(prediction)


# spaCy 
# each word should have: describers, actions, objects-of-actions, 
#                        actions-received, subjects-of-actions-received
