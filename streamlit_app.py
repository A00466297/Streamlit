import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib 
import os

# To load the Iris dataset
def get_model():

    if os.path.exists('iris.joblib'):
        classifier = joblib.load('iris.joblib')
    else:
        data = load_iris()
        X = pd.DataFrame(data.data, columns=data.feature_names)
        y = pd.Series(data.target, name='class')
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=35, shuffle=True)
        classifier = DecisionTreeClassifier().fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        acc = accuracy_score(y_pred, y_test)
        con_matrix = confusion_matrix(y_test, y_pred)
        joblib.dump(classifier, 'iris.joblib')
    return classifier

def app():
    data = load_iris()
    classifier = get_model()
    st.title("Classification using Iris dataset")

    sepal_length = st.slider("Sepal length", 0.0, 10.0, 5.0)
    sepal_width = st.slider("Sepal width", 0.0, 10.0, 5.0)
    petal_length = st.slider("Petal length", 0.0, 10.0, 5.0)
    petal_width = st.slider("Petal width", 0.0, 10.0, 5.0)

    prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    st.write(f"Predicted class: {data.target_names[prediction[0]]}")

if __name__ == '__main__':
    app()

