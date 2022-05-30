import numpy as np
import feature_extraction
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split
global X_la
def getResult(url):
    global X_la
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

    X_new=feature_extraction.generate_dataset(X_input)
    print(X_new)
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

print(getResult('https://stackoverflow.com/questions/16743889/cant-use-scikit-learn-attributeerror-module-object-has-no-attribute'))
print(X_la)
data=''
print(X_la[0])
if X_la[0][0]=='-1':
    data+='●Змогли отримати інформацію о IP адресі сервісу ❌\n'
else:
    data+='●Не змогли отримати інформацію о IP адресі сервісу ✅\n'

print(X_la[0][0])

if X_la[0][2]=='-1':
    data+='●Посилання було скорочено ❌\n'
else:
    data+='●Посилання не було скорочено ✅\n'


if X_la[0][3]=='1':
    data+='●Посилання не має символу "@" ✅\n'
else:
    data+='●Посилання має "@" ❌\n'

if X_la[0][4]=='1':
    data+='●Посилання не має "//" ✅\n'
else:
    data+='●Посилання має "//" ❌\n'

if X_la[0][5]=='1':
    data+='●Посилання не має префіксів(суфіксів) ✅\n'
else:
    data+='●Посилання має префікси(суфікси)"//" ❌\n'

if X_la[0][6] == '1':
    data += '●Посилання має один субдомен ✅\n'
elif X_la[0][6] == '0':
    data += '●Посилання має два субдомена ✅\n'
else:
    data += '●Посилання має більше двох субдоменів ❌\n'

if X_la[0][7] == '1':
    data += '●Отримали контент запитуваної сторінки ✅\n'
else:
    data += '●Не отримали контент запитуваної сторінки ❌\n'

if X_la
print(data)