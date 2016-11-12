import numpy as np
import pandas as pd
import matplotlib as plt

from sklearn.datasets import load_iris
iris_dataset = load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
	iris_dataset['data'], iris_dataset['target'], random_state=0)

#iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
#grr = pd.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='o',
#	hist_kwds ={'bins': 20}, s=60, alpha=.8)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_new = np.array([[5, 2.9, 1, 0.2]])

prediction = knn.predict(X_new)
print("Predicted target name: {}".format(iris_dataset['target_names'][prediction]))

y_pred = knn.predict(X_test)
print("Test set predictions:\n {}".format(y_pred))

print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))

