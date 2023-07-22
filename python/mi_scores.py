# -*- coding: utf-8 -*-
"""
For calculation of mutual information scores
Created on Sat Jul 22 19:27:12 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

How to run:
python mi_scores.py --help
python mi_scores.py -c .\corpus\sentiment\sentiment_my_dataset.csv -n 30

Reference:
https://medium.com/@tejpal.abhyuday/information-theory-explained-for-machine-learning-a1bd8e7cd242

"""

import numpy as np
import pandas as pd
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import mutual_info_classif

def compute_MI(corpus_filename, N):
    # Read dataset
    df = pd.read_csv(corpus_filename)
    texts, labels = df['text'].values, df['sentiment'].values

    # Vectorize the texts without additional tokenization (relying on whitespace)
    vectorizer = CountVectorizer(tokenizer=lambda x: x.split(), preprocessor=lambda x: x)
    X = vectorizer.fit_transform(texts)

    # Compute mutual information scores
    mi_scores = mutual_info_classif(X, labels, discrete_features=True)
    
    # Get the top N words based on the MI scores
    top_N_indices = mi_scores.argsort()[-N:][::-1]
    top_N_words = np.array(vectorizer.get_feature_names_out())[top_N_indices]
    top_N_scores = mi_scores[top_N_indices]

    return top_N_words, top_N_scores

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compute top N words with highest mutual information.')
    parser.add_argument('-c', '--corpus_filename', required=True, help='Path to the input CSV corpus file.')
    parser.add_argument('-n', '--top_N_words', type=int, required=True, help='Number of top words to be extracted based on MI.')
    args = parser.parse_args()

    top_words, top_scores = compute_MI(args.corpus_filename, args.top_N_words)
    
    for word, score in zip(top_words, top_scores):
        print(f"{word}: {score:.4f}")

