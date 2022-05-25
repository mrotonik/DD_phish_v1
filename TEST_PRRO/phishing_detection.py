import numpy as np
import feature_extraction
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split

def getResult(url):

    data = np.loadtxt("dataset.csv", delimiter = ",")
    X = data[: , :-1]
    y = data[: , -1]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    clf = rfc()
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    print(score*100)

    X_new = []

    X_input = url
    X_new=feature_extraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1,-1)
    print('===========')
    print(X_new[0][:17])
    print(X_new[0][18:])
    print('===========')
    X_la=[[]]
    for i in range(len(X_new[0])):
        if i!=17:
            X_la[0].append(X_new[0][i])
        else:
            X_la[0].append('1')
    print(X_la)
    try:
        prediction = clf.predict(X_la)
        if prediction == -1:
            return "Phishing Url"
        else:
            return "Legitimate Url"
    except:
        return "Phishing Url"
