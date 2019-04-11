import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import linear_model, model_selection

def adult_d(age,workclass,education,occupation,race,sex,hoursperweek,income):
    names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation',
             'relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','income']
    df = pd.read_csv('../Data/adult.data.txt',header=None,names=names)
    df = df[['age','workclass','education','occupation','race','sex','hours-per-week','income']]

    new_df = pd.get_dummies(df)

    x = new_df.iloc[:,:-2]
    y = new_df.iloc[:,-1]

    train_x, test_x, train_y, test_y = model_selection.train_test_split(x,y)

    lr = linear_model.LogisticRegression()
    lr.fit(train_x,train_y)         # 훈련은 위한 데이터 fit..

    n = [[age,workclass,education,occupation,race,sex,hoursperweek,income]]
    n_df = pd.DataFrame(n,columns=['age','workclass','education','occupation','race','sex','hours-per-week','income'])

    df2 = df.append(n_df)
    one_hot= pd.get_dummies(df2)
    pred_x = np.array(one_hot.iloc[-1,:-2]).reshape(1,-1)
    pred_y = lr.predict(pred_x)
    return pred_y