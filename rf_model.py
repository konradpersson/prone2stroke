import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import StandardScaler,LabelEncoder
from imblearn.over_sampling import SMOTE #needs installing of imbalanced-learn
import scikitplot as skplt #needs installing of scikit-plot
import os
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score, recall_score, roc_auc_score, precision_score, f1_score
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model():
    con = sqlite3.connect('prone-to-stroke.db')

    #df 
    df = pd.read_sql_quert('SELECT * FROM dataset')

    # Encoding categorical values 
    df['gender'] = df['gender'].replace({'Male':0,'Female':1,'Other':-1}).astype(np.uint8)
    df['Residence_type'] = df['Residence_type'].replace({'Rural':0,'Urban':1}).astype(np.uint8)
    df['work_type'] = df['work_type'].replace({'Private':0,'Self-employed':1,'Govt_job':2,'children':-1,'Never_worked':-2}).astype(np.uint8)
    df['ever_married'] = df['ever_married'].replace({'Yes':1, 'No':0}).astype(np.uint8)
    df['smoking_status'] = df['smoking_status'].replace({'smokes':2,'formerly smoked':1,'never smoked':0}).astype(np.uint8)

    #Feature Scaling 
    X  = df[['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi', 'smoking_status']]
    y = df['stroke']

    #Splitting into train and test 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=4)

    #fixing biased data 
    oversample = SMOTE()
    X_train_resh, y_train_resh = oversample.fit_resample(X_train, y_train.ravel())

    # Scale data in pipeline 
    rf_pipeline = Pipeline(steps = [('scale',StandardScaler()),('RF',RandomForestClassifier(random_state=42))])
    rf_cv = cross_val_score(rf_pipeline,X_train_resh,y_train_resh,cv=10,scoring='f1')

    #Random forest Classifier 
    model = RandomForestClassifier(max_features=2,n_estimators=100,bootstrap=True)

    model.fit(X_train_resh,y_train_resh)

    model_tuned_pred = model.predict(X_test)

    #Model interpretation LIME
    import lime
    import lime.lime_tabular

    # LIME has one explainer for all the models
    explainer = lime.lime_tabular.LimeTabularExplainer(X.values, feature_names=X.columns.values.tolist(),
                                                      class_names=['Not going to get stroke','Possibility of stroke'], verbose=True, mode='classification')


    con.close()

def predict(gender, age, hypertension, heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status):
      Test = pd.DataFrame([[gender, age, hypertension, heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])
      exp = explainer.explain_instance(
      data_row=Test.iloc[0], 
      predict_fn=rf_pipeline.predict_proba
      )

      exp.show_in_notebook(show_table=True) # what to do here???? exp Class? to be continued...
      
      
      