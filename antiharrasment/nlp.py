import numpy as np 
# import matplotlib.pyplot as plt
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
nltk.download('stopwords')
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix

from .models import query as querydbset

def pred(statement):
    dataset = querydbset.objects.all()

    corpus = []
    for query in dataset:
        sstatement = re.sub('[^a-zA-Z]', ' ', query.statement).lower().split()
        ps = PorterStemmer()
        sstatement = ' '.join([ps.stem(word) for word in sstatement if not word in set(stopwords.words('english'))])
        corpus.append(sstatement)

    uniqueWords = {}
    count = 0
    for line in corpus:
        for word in line.split(' '):
            if word not in uniqueWords.keys():
                uniqueWords[word] = count
                count += 1

    train_input_vector = []
    for line in corpus:
        arr = np.zeros(count)
        for word in line.split(' '):
            arr[uniqueWords[word]] = 1
        train_input_vector.append(arr)

    train_input = np.array(train_input_vector)

    sigmoid = lambda x: 1/(1+np.exp(-x))
    sigmoid_graph = lambda x: x*(1-x)

    y = [1 if x.is_harrassing else 0 for x in dataset]

    max_iter = 10000
    learning_rate = 0.3
    intercept = np.ones((train_input.shape[0],1))
    train_input = np.hstack((intercept, train_input))
    theta = np.zeros(train_input.shape[1])
    train_Y_arr = np.array(y)
    for iter in range(max_iter):
        current_val = np.dot(train_input,theta)
        current_predictions = sigmoid(current_val)
        #Update Theta
        error = train_Y_arr - current_predictions
        gradient = np.dot(train_input.T, error)
        theta += learning_rate * gradient

    test_input_vector = []
    arr = np.zeros(count)

    sstatement = re.sub('[^a-zA-Z]', ' ', statement).lower().split()
    ps = PorterStemmer()
    sstatement = ' '.join([ps.stem(word) for word in sstatement if not word in set(stopwords.words('english'))])
    
    for word in sstatement.split(' '):
        if word in uniqueWords:
            arr[uniqueWords[word]] = 1
    test_input_vector.append(arr)

    test_input = np.array(test_input_vector)
    intercept = np.ones((test_input.shape[0],1))
    test_input = np.hstack((intercept, test_input))
    final_cost = np.dot(test_input, theta)
    prediction = np.round(sigmoid(final_cost))

    return prediction[0] > 0.0