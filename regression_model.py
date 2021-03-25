import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import numpy as np

sc = StandardScaler()

classifier = LogisticRegression(random_state=0)

def train_model():
    con = sqlite3.connect('prone-to-stroke-dataset.db')
    
    #df = dataframe
    df = pd.read_sql_query('SELECT * FROM dataset', con)
    
    df['gender'] = df['gender'].replace({'Male':0,'Female':1,'Other':-1}).astype(np.uint8)
    df['residence_type'] = df['residence_type'].replace({'Rural':0,'Urban':1}).astype(np.uint8)
    df['work_type'] = df['work_type'].replace({'Private':0,'Self-employed':1,'Govt_job':2,'children':-1,'Never_worked':-2}).astype(np.uint8)
    df['smoking_status'] = df['smoking_status'].replace({'smokes':2,'formerly smoked':1,'never smoked':0}).astype(np.uint8)
    df['ever_married'] = df['ever_married'].replace({'Yes':1,'No':0}).astype(np.uint8)

    # Independent values
    X  = df[['gender','age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']]
    # X = df.iloc[:, :-1].values


    # Dependent values
    y = df['stroke']
    #y = df.iloc[:, -1].values


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)

    # Scale the data to fit the training algorithm
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    # Training the model
    classifier.fit(X_train, y_train)

    con.close()

def predict(gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status):

    probability_of_click = classifier.predict_proba(sc.transform([[gender, age, hypertension, heart_disease, ever_married, work_type, avg_glucose_level, residence_type, avg_glucose_level, bmi, smoking_status]]))

    probability = probability_of_click[0, 1]

    prediction = True if probability > 0.5 else False

    return { "willClick": prediction, "probability": probability }