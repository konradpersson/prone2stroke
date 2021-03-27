
# Importing Packages
import sqlite3
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE #needs installing of imbalanced-learn
#Model interpretation LIME
import lime
import lime.lime_tabular

# Random forest Classifier 
model = RandomForestClassifier(max_features=2,n_estimators=100,bootstrap=True)

def train_model():
    con = sqlite3.connect('prone-to-stroke-dataset.db')

    # Creating dataframe from Database 
    df = pd.read_sql_query('SELECT * FROM dataset', con)

    # Encoding categorical values 
    df['gender'] = df['gender'].replace({'Male':0,'Female':1,'Other':-1}).astype(np.uint8)
    df['residence_type'] = df['residence_type'].replace({'Rural':0,'Urban':1}).astype(np.uint8)
    df['work_type'] = df['work_type'].replace({'Private':0,'Self-employed':1,'Govt_job':2,'children':-1,'Never_worked':-2}).astype(np.uint8)
    df['smoking_status'] = df['smoking_status'].replace({'smokes':2,'formerly smoked':1,'never smoked':0}).astype(np.uint8)


    #Feature Scaling (removing columns of lowest importance since it gives the best result)
    X  = df[['gender','age','work_type','residence_type','avg_glucose_level','bmi', 'smoking_status']]
    y = df['stroke']

    # Splitting into train and test 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)


    # Fixing biased data 
    oversample = SMOTE()
    X_train_resh, y_train_resh = oversample.fit_resample(X_train, y_train.ravel())
    
  
        
    model.fit(X_train_resh,y_train_resh)

    model_tuned_pred = model.predict(X_test)
    
    # LIME has one explainer for all the models
    explainer = lime.lime_tabular.LimeTabularExplainer(X.values, feature_names=X.columns.values.tolist(),
                                                      class_names=['Not going to get stroke','Possibility of stroke'], verbose=True, mode='classification') 
 
    con.close()

def predict(gender, age, work_type,residence_type,avg_glucose_level,bmi,smoking_status):
    
    #gender, age, hypertension, heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_s
    model.predict_proba([[gender, age, work_type,residence_type,avg_glucose_level,bmi,smoking_status]])
     
      
    #probability = probability_of_stroke[0, 1]
    
    #prediction = True if probability > 0.5 else False
    
    #return { "willGetStroke": prediction, "probability": probability }
      
      