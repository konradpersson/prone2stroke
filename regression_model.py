import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

sc = StandardScaler()

classifier = LogisticRegression(random_state=0)

def train_model():
    con = sqlite3.connect('ads_dataset.db')
    
    #df = dataframe
    df = pd.read_sql_query('SELECT * FROM dataset', con)

    # Independent values
    X = df.iloc[:, :-1].values

    # Dependent values
    y = df.iloc[:, -1].values


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    # Scale the data to fit the training algorithm
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the model
    classifier.fit(X_train, y_train)

    con.close()

def predict(age, income):

    probability_of_click = classifier.predict_proba(sc.transform([[age, income]]))

    probability = probability_of_click[0, 1]

    prediction = True if probability > 0.5 else False

    return { "willClick": prediction, "probability": probability }