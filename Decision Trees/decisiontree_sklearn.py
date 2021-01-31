import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt

data = datasets.load_breast_cancer()
X, y = pd.DataFrame(data.data, columns=data.feature_names), pd.DataFrame(data.target, columns=['label'])
X_train, X_test, y_train, y_test = train_test_split(X, y)
print("X_train size :", len(X_train))
print("X_test size :", len(X_test))
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print('Accuracy :', accuracy_score(y_test, y_pred))
print('F1 Score :', f1_score(y_test, y_pred, average='macro'))

fig = plt.figure(figsize=(25, 20))
_ = plot_tree(clf, feature_names=data.feature_names,
              class_names=data.target_names, filled=True)
fig.savefig('sklearn_dt.png')
