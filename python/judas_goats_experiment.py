# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 11:38:35 2023
@author: Ye Kyaw Thu, LU Lab., Myanmar

How to run:
python judas_goats_experiment.py breast_cancer
python judas_goats_experiment.py diabetes
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine, load_digits, load_breast_cancer, load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.cluster import KMeans
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import sys

def plot_decision_boundaries(ax, model, data, labels, title):
    # Create a mesh grid for the data
    x_min, x_max = data[:, 0].min() - 1, data[:, 0].max() + 1
    y_min, y_max = data[:, 1].min() - 1, data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))

    # Predict the model output for the entire grid
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # Plot the decision boundaries
    ax.contourf(xx, yy, Z, alpha=0.4)
    ax.scatter(data[:, 0], data[:, 1], c=labels, edgecolors='k')
    ax.set_title(title)

def load_and_prepare_data(dataset_name):
    if dataset_name == "iris":
        data, labels = load_iris(return_X_y=True)
    elif dataset_name == "wine":
        data, labels = load_wine(return_X_y=True)
    elif dataset_name == "digits":
        data, labels = load_digits(return_X_y=True)
    elif dataset_name == "breast_cancer":
        data, labels = load_breast_cancer(return_X_y=True)
    elif dataset_name == "diabetes":
        data, labels = load_diabetes(return_X_y=True)
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    pca = PCA(n_components=2)
    data_2d = pca.fit_transform(scaled_data)

    return data, labels, data_2d, scaler, pca

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a dataset name: iris, wine, digits, breast_cancer, or diabetes")
        sys.exit(1)

    dataset_name = sys.argv[1]
    data, labels, data_2d, scaler, pca = load_and_prepare_data(dataset_name)

    np.random.seed()
    unique_labels = np.unique(labels)
    juda_goats_indices = [np.random.choice(np.where(labels == i)[0]) for i in unique_labels]
    juda_goats = data[juda_goats_indices]
    juda_goats_labels = labels[juda_goats_indices]
    juda_goats_2d = pca.transform(scaler.transform(juda_goats))

    fig, axes = plt.subplots(5, 2, figsize=(12, 30))

    algorithms = [
        ('SVM', SVC(kernel='linear', C=1e5), SVC(kernel='linear', C=1)),
        ('GaussianNB', GaussianNB(), GaussianNB()),
        ('KMeans', KMeans(n_clusters=len(unique_labels), init=juda_goats_2d, n_init=1, max_iter=300),
         KMeans(n_clusters=len(unique_labels), n_init=10, max_iter=300)),
        ('Logistic Regression', LogisticRegression(max_iter=10000), LogisticRegression(max_iter=10000)),
        ('Random Forest', RandomForestClassifier(), RandomForestClassifier())
    ]

    for i, (name, juda, full) in enumerate(algorithms):
        juda.fit(juda_goats_2d, juda_goats_labels)
        full.fit(data_2d, labels)

        # Plot decision boundaries
        if name in ['SVM', 'GaussianNB', 'Logistic Regression', 'Random Forest']:
            plot_decision_boundaries(axes[i, 0], juda, data_2d, labels, f'{name} with Juda Goats')
            plot_decision_boundaries(axes[i, 1], full, data_2d, labels, f'{name} without Juda Goats')
        
            print(f"\nResults with Juda Goats using {name}:\n")
            print("Accuracy:", accuracy_score(labels, juda.predict(data_2d)))
            print(confusion_matrix(labels, juda.predict(data_2d)))

            print(f"\nResults without Juda Goats using {name}:\n")
            print("Accuracy:", accuracy_score(labels, full.predict(data_2d)))
            print(confusion_matrix(labels, full.predict(data_2d)))
        elif name == 'KMeans':
            juda_labels = juda.predict(data_2d)
            full_labels = full.predict(data_2d)
        
            plot_decision_boundaries(axes[i, 0], juda, data_2d, juda_labels, f'{name} with Juda Goats')
            plot_decision_boundaries(axes[i, 1], full, data_2d, full_labels, f'{name} without Juda Goats')

            print(f"\nResults with Juda Goats using {name}:\n")
            print("Accuracy:", accuracy_score(labels, juda_labels))
            print(confusion_matrix(labels, juda_labels))

            print(f"\nResults without Juda Goats using {name}:\n")
            print("Accuracy:", accuracy_score(labels, full_labels))
            print(confusion_matrix(labels, full_labels))
    plt.savefig("results.png")
    plt.show()
