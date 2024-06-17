import joblib

model = joblib.load('model/tuned_logreg_model.joblib')

def prediction(data):
    """Making prediction
    
    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data
    
    Returns:
        str: Prediction result (Dropout, Graduate)
    """
    
    result = model.predict(data)
    final_result = 'Yes' if result==1 else 'No'
    return final_result