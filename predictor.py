import pandas as pd
import numpy as np
import joblib
import sklearn
import os

def predict(hashtable,models_config):
    data = pd.DataFrame.from_dict(hashtable)
    model_hashtable={1:"Linear Regression",2:"Decision Tree Regression", 3:"Random Forest Regression", 4: "KNN Regression", 5:"Support Vector Regression", 6:"XGBoost Regression"}
    preds=[]
    for i in range(1,6):
        filename = 'model'+str(i)+'.pkl'
        file_path = os.path.join(models_config, filename)
        model_enc=joblib.load(file_path) 
        model=model_enc[0]
        ct=model_enc[1]
        sc=model_enc[2]
        dataenc= pd.DataFrame(ct.transform(data).toarray())
        dataenc = sc.transform(dataenc)

        X = dataenc
        prediction = int(np.round(model.predict(X)))
        preds.append(prediction)

    return preds,model_hashtable

