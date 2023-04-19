import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
import joblib

iris_data = load_iris()

X = iris_data['data']
y = iris_data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)

classifier = tree.DecisionTreeClassifier().fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print(accuracy_score(y_pred, y_test))
print(confusion_matrix(y_test, y_pred))
print(iris_data['target_names'][y_pred])

joblib.dump(classifier, 'iris.joblib')
tree.plot_tree(classifier)
plt.show()
