import joblib
import numpy as np
import pandas as pd

encoder_Application_mode = joblib.load('model/encoder_Application_mode.joblib')
encoder_Course = joblib.load('model/encoder_Course.joblib')
encoder_Daytime_evening_attendance = joblib.load('model/encoder_Daytime_evening_attendance.joblib')
encoder_Debtor = joblib.load('model/encoder_Debtor.joblib')
encoder_Displaced = joblib.load('model/encoder_Displaced.joblib')
encoder_Educational_special_needs = joblib.load('model/encoder_Educational_special_needs.joblib')
encoder_Fathers_occupation = joblib.load('model/encoder_Fathers_occupation.joblib')
encoder_Fathers_qualification = joblib.load('model/encoder_Fathers_qualification.joblib')
encoder_Gender = joblib.load('model/encoder_Gender.joblib')
encoder_International = joblib.load('model/encoder_International.joblib')
encoder_Marital_status = joblib.load('model/encoder_Marital_status.joblib')
encoder_Mothers_occupation = joblib.load('model/encoder_Mothers_occupation.joblib')
encoder_Mothers_qualification = joblib.load('model/encoder_Mothers_qualification.joblib')
encoder_Nacionality = joblib.load('model/encoder_Nacionality.joblib')
encoder_Previous_qualification = joblib.load('model/encoder_Previous_qualification.joblib')
encoder_Scholarship_holder = joblib.load('model/encoder_Scholarship_holder.joblib')
encoder_Tuition_fees_up_to_date = joblib.load('model/encoder_Tuition_fees_up_to_date.joblib')

pca = joblib.load('model/pca.joblib')

scaler_Admission_grade = joblib.load('model/scaler_Admission_grade.joblib')
scaler_Age_at_enrollment = joblib.load('model/scaler_Age_at_enrollment.joblib')
scaler_Application_order = joblib.load('model/scaler_Application_order.joblib')
scaler_Curricular_units_1st_sem_approved = joblib.load('model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_Curricular_units_1st_sem_credited = joblib.load('model/scaler_Curricular_units_1st_sem_credited.joblib')
scaler_Curricular_units_1st_sem_enrolled = joblib.load('model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_Curricular_units_1st_sem_evaluations = joblib.load('model/scaler_Curricular_units_1st_sem_evaluations.joblib')
scaler_Curricular_units_1st_sem_grade = joblib.load('model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_Curricular_units_1st_sem_without_evaluations = joblib.load('model/scaler_Curricular_units_1st_sem_without_evaluations.joblib')
scaler_Curricular_units_2nd_sem_approved = joblib.load('model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_Curricular_units_2nd_sem_credited = joblib.load('model/scaler_Curricular_units_2nd_sem_credited.joblib')
scaler_Curricular_units_2nd_sem_enrolled = joblib.load('model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_Curricular_units_2nd_sem_evaluations = joblib.load('model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_Curricular_units_2nd_sem_grade = joblib.load('model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_Curricular_units_2nd_sem_without_evaluations = joblib.load('model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib')
scaler_GDP = joblib.load('model/scaler_GDP.joblib')
scaler_Inflation_rate = joblib.load('model/scaler_Inflation_rate.joblib')
scaler_Previous_qualification_grade = joblib.load('model/scaler_Previous_qualification_grade.joblib')
scaler_Unemployment_rate = joblib.load('model/scaler_Unemployment_rate.joblib')

encoder_target = joblib.load('model/encoder_target.joblib')

quanti_columns = ['Application_order', 'Previous_qualification_grade', 'Admission_grade', 'Age_at_enrollment', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate', 'Inflation_rate', 'GDP']

def data_preprocessing(data):
    """Preprocessing data
    
    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction

    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    # Qualitative
    df['Marital_status'] = [encoder_Marital_status.transform(np.array(data['Marital_status'][0]).reshape(-1))[0]]
    df['Application_mode'] = [encoder_Application_mode.transform(np.array(data['Application_mode']).reshape(-1))[0]]
    df['Course'] = [encoder_Course.transform(np.array(data['Course']).reshape(-1))[0]]
    df['Daytime_evening_attendance'] = [encoder_Daytime_evening_attendance.transform(np.array(data['Daytime_evening_attendance']).reshape(-1))[0]]
    df['Previous_qualification'] = [encoder_Previous_qualification.transform(np.array(data['Previous_qualification']).reshape(-1))[0]]
    df['Nacionality'] = [encoder_Nacionality.transform(np.array(data['Nacionality']).reshape(-1))[0]]
    df['Mothers_qualification'] = [encoder_Mothers_qualification.transform(np.array(data['Mothers_qualification']).reshape(-1))[0]]
    df['Fathers_qualification'] = [encoder_Fathers_qualification.transform(np.array(data['Fathers_qualification']).reshape(-1))[0]]
    df['Mothers_occupation'] = [encoder_Mothers_occupation.transform(np.array(data['Mothers_occupation']).reshape(-1))[0]]
    df['Fathers_occupation'] = [encoder_Fathers_occupation.transform(np.array(data['Fathers_occupation']).reshape(-1))[0]]
    df['Displaced'] = [encoder_Displaced.transform(np.array(data['Displaced']).reshape(-1))[0]]
    df['Educational_special_needs'] = [encoder_Educational_special_needs.transform(np.array(data['Educational_special_needs']).reshape(-1))[0]]
    df['Debtor'] = [encoder_Debtor.transform(np.array(data['Debtor']).reshape(-1))[0]]
    df['Tuition_fees_up_to_date'] = [encoder_Tuition_fees_up_to_date.transform(np.array(data['Tuition_fees_up_to_date']).reshape(-1))[0]]
    df['Gender'] = [encoder_Gender.transform(np.array(data['Gender']).reshape(-1))[0]]
    df['Scholarship_holder'] = [encoder_Scholarship_holder.transform(np.array(data['Scholarship_holder']).reshape(-1))[0]]
    df['International'] = [encoder_International.transform(np.array(data['International']).reshape(-1))[0]]
    
    # Quantitative
    data['Admission_grade'] = scaler_Admission_grade.transform(np.asarray(data['Admission_grade']).reshape(-1,1))[0]
    data['Age_at_enrollment'] = scaler_Age_at_enrollment.transform(np.asarray(data['Age_at_enrollment']).reshape(-1,1))[0]
    data['Application_order'] = scaler_Application_order.transform(np.asarray(data['Application_order']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_approved'] = scaler_Curricular_units_1st_sem_approved.transform(np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_credited'] = scaler_Curricular_units_1st_sem_credited.transform(np.asarray(data['Curricular_units_1st_sem_credited']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_enrolled'] = scaler_Curricular_units_1st_sem_enrolled.transform(np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_evaluations'] = scaler_Curricular_units_1st_sem_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_evaluations']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_grade'] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1,1))[0]
    data['Curricular_units_1st_sem_without_evaluations'] = scaler_Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data['Curricular_units_1st_sem_without_evaluations']).reshape(-1,1))[0]
    data['Curricular_units_2nd_sem_approved'] = scaler_Curricular_units_2nd_sem_approved.transform(np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1,1))[0]
    data['Curricular_units_2nd_sem_credited'] = scaler_Curricular_units_2nd_sem_credited.transform(np.asarray(data['Curricular_units_2nd_sem_credited']).reshape(-1,1))[0]
    data['Curricular_units_2nd_sem_grade'] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1,1))[0]
    data['Curricular_units_2nd_sem_without_evaluations'] = scaler_Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data['Curricular_units_2nd_sem_without_evaluations']).reshape(-1,1))[0]
    data['GDP'] = scaler_GDP.transform(np.asarray(data['GDP']).reshape(-1,1))[0]
    data['Inflation_rate'] = scaler_Inflation_rate.transform(np.asarray(data['Inflation_rate']).reshape(-1,1))[0]
    data['Previous_qualification_grade'] = scaler_Previous_qualification_grade.transform(np.asarray(data['Previous_qualification_grade']).reshape(-1,1))[0]
    data['Unemployment_rate'] = scaler_Unemployment_rate.transform(np.asarray(data['Unemployment_rate']).reshape(-1,1))[0]

    df[['pc_1', 'pc_2', 'pc_3', 'pc_4', 'pc_5']] = pca.transform(data[quanti_columns])
    
    return df