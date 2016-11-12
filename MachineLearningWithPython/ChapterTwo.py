import numpy as np
import random
import mglearn
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

#print("cancer.keys(): \n{}".format(cancer.keys()))

#print("Shape of cancer data: {}".format(cancer.data.shape))

#print("Sample counts per class:\n{}".format(
#		{n: v for n, v in zip(cancer.target_names, np.bincount(cancer.target))}))

#print("Feature names:\n{}".format(cancer.feature_names))

#from sklearn.datasets import load_boston
#boston = load_boston()
#print("Data shape: {}".format(boston.data.shape))

#X, y = mglearn.datasets.load_extended_boston()
#print("X.shape: {}".format(X.shape))

#mglearn.plots.plot_knn_classification(n_neighbors=1)

from sklearn.model_selection import train_test_split

#X, y = mglearn.datasets.make_forge()
#X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
#clf = KNeighborsClassifier(n_neighbors=3)

#clf.fit(X_train, y_train)
#print("Test set predictions: {}".format(clf.predict(X_test)))
#print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))

#fig, axes = plt.subplots(1, 3, figsize=(10, 3))
#for n_neighbors, ax in zip([1, 3, 9], axes):
#	clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X,y)
#	mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
#	mglearn.discrete_scatter(X[:,0], X[:,1], y, ax=ax)
#	ax.set_title("{} neighbors(s)".format(n_neighbors))
#	ax.set_xlabel("feature 0")
#	ax.set_ylabel("feature 1")
#axes[0].legend(loc=3)

#plt.show()

X_train, X_test, y_train, y_test = train_test_split(
	cancer.data, cancer.target, stratify=cancer.target, random_state=66)

training_accuracy = []
test_accuracy = []
neighbors_settings = range(1, 11)

for n_neighbors in neighbors_settings:
	clf = KNeighborsClassifier(n_neighbors=n_neighbors)
	clf.fit(X_train, y_train)
	training_accuracy.append(clf.score(X_train, y_train))
	test_accuracy.append(clf.score(X_test, y_test))

#plt.plot(neighbors_settings, training_accuracy, label="training accuracy")
#plt.plot(neighbors_settings, test_accuracy, label="test accuracy")
#plt.ylabel("Accuracy")
#plt.xlabel("n_neighbors")
#mglearn.plots.plot_knn_regression(n_neighbors=1)
#mglearn.plots.plot_knn_regression(n_neighbors=3)
#plt.show()

from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)

print("Test set predictions:\n{}".format(reg.predict(X_test)))

print("Test set R2: {:.2f}".format(reg.score(X_test, y_test)))

fig, axes = plt.subplots(1, 3, figsize=(15,4))
line = np.linspace(-3, 3, 1000).reshape(-1, 1)
for n_neighbors, ax in zip([1, 3, 9], axes):
	reg = KNeighborsRegressor(n_neighbors=n_neighbors)
	reg.fit(X_train, y_train)
	ax.plot(line, reg.predict(line))
	ax.plot(X_train, y_train, '^', c=mglearn.cm2(0), markersize=8)
	ax.plot(X_test, y_test, 'v', c=mglearn.cm2(1), markersize=8)

	ax.set_title(
		"{} neighbors(s)\n train score: {:.2f} test score: {:.2f}".format(
			n_neighbors, reg.score(X_train, y_train),reg.score(X_test, y_test)))
	ax.set_xlabel("Feature")
	ax.set_ylabel("Target")
axes[0].legend(["Model predictions", "Training data/target",
				"Test data/target"], loc="best")

plt.show()

