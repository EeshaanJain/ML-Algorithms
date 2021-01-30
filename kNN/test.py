import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from knn import KNN


iris = datasets.load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

accuracy = np.sum(predictions == y_test) / len(y_test)
print(accuracy*100)



# my_cmap = ListedColormap(["#FF781F", "#149414", "#52307C"])
# plt.figure()
# # Displaying 2 out of 4 features so that we can see in 2D
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=my_cmap, edgecolor='k', s=20)
# plt.show()
