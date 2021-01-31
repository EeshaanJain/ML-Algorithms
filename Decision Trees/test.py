import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from decisiontree import DecisionTree
import matplotlib.pyplot as plt

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true==y_pred)/len(y_true)
    return accuracy

data = datasets.load_breast_cancer()
X = data.data
y = data.target
print(X.shape)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
accuracies = []
for depth in range(1,31):
    tree = DecisionTree(max_depth=depth)
    tree.fit(X_train, y_train)
    y_pred = tree.predict(X_test)
    acc = accuracy(y_test, y_pred)
    accuracies.append(acc)
    print(f"Accuracy for depth {depth} : {acc:.2f}")

plt.figure()
plt.plot(range(1,31), accuracies)
plt.xlabel('Max Depth of Tree')
plt.ylabel('Accuracy')
plt.title('Performance of Decision Tree on Breast Cancer dataset')
plt.savefig('dt_bc.png')
plt.show()
