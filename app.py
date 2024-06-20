import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import streamlit as st
import data_preprocessing as dp
from prediction import prediction
sns.set(style='dark')

import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    # Add a logo
    st.image("asset/education logo.png")
    
    selected = option_menu(
        menu_title = 'Menu',
        options = ['Dashboard', 'Predict'],
        icons = ['clipboard2-data', 'calculator'],
        menu_icon = 'menu-up',
        default_index = 0
    )

if selected == 'Dashboard':
    df = pd.read_csv("data/data_clean.csv")

    st.title("Student's Dropout Dashboard")

    container = st.container()
    all = st.checkbox('Select all', value=True)
    if all:
        selected_course = container.multiselect(
            'Courses',
            df['Course'].unique(),
            df['Course'].unique()
        )
    else:
        selected_course = container.multiselect(
            'Coures',
            df['Course'].unique()
        )
    df = df[df['Course'].isin(selected_course)]

    col1, col2 = st.columns(2)
    with col1:
        total_student = len(df)
        st.metric('Total students', value=f'{total_student:,}')
    with col2:
        status_counts = df['Status'].value_counts().reset_index()
        base = alt.Chart(status_counts).mark_arc(innerRadius=50).encode(
            theta=alt.Theta(field='count', type='quantitative'),
            color=alt.Color(field='Status', type='nominal', 
                            scale=alt.Scale(domain=status_counts['Status'].values, range=['#2FF3E0','#F51720']))
        )
        text = base.mark_text(radius=140, size=20).encode(text='count')
        chart = base + text
        st.altair_chart(chart, theme='streamlit', use_container_width=True)

    chart = alt.Chart(df).mark_bar().encode(
        y='Application_mode',
        x='count(Course)',
        color=alt.Color(field='Status', type='nominal', 
                        scale=alt.Scale(domain=status_counts['Status'].values, 
                                        range=['#2FF3E0','#F51720']), legend=None),    
    )
    st.altair_chart(chart, theme='streamlit', use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        chart = alt.Chart(df).mark_bar().encode(
            x='Gender',
            y=alt.X('count(Course)', stack='normalize'),
            color=alt.Color(field='Status', type='nominal', 
                            scale=alt.Scale(domain=status_counts['Status'].values, 
                            range=['#2FF3E0','#F51720']), legend=None),
        )
        st.altair_chart(chart, use_container_width=True)
    with col2:
        chart = alt.Chart(df).mark_bar().encode(
            x='Tuition_fees_up_to_date',
            y=alt.X('count(Course)', stack='normalize').axis(title=None),
            color=alt.Color(field='Status', type='nominal', 
                            scale=alt.Scale(domain=status_counts['Status'].values, 
                            range=['#2FF3E0','#F51720']), legend=None),
        )
        st.altair_chart(chart, use_container_width=True)
    with col3:
        chart = alt.Chart(df).mark_bar().encode(
            x='Scholarship_holder',
            y=alt.X('count(Course)', stack='normalize').axis(title=None),
            color=alt.Color(field='Status', type='nominal', 
                            scale=alt.Scale(domain=status_counts['Status'].values, 
                            range=['#2FF3E0','#F51720']), legend=None),
        )
        st.altair_chart(chart, use_container_width=True)
    with col4:
        chart = alt.Chart(df).mark_bar().encode(
            x='Debtor',
            y=alt.X('count(Course)', stack='normalize').axis(title=None),
            color=alt.Color(field='Status', type='nominal', 
                            scale=alt.Scale(domain=status_counts['Status'].values, 
                            range=['#2FF3E0','#F51720']), legend=None),
        )
        st.altair_chart(chart, use_container_width=True)

    df_scatter = df[(df['Curricular_units_1st_sem_grade']!=0) & (df['Curricular_units_2nd_sem_grade']!=0)]
    chart = alt.Chart(df_scatter).mark_circle(size=15).encode(
        x=alt.X('Curricular_units_1st_sem_grade', 
                scale=alt.Scale(domain=[df_scatter['Curricular_units_1st_sem_grade'].min(),
                                        df_scatter['Curricular_units_1st_sem_grade'].max()])),
        y=alt.Y('Curricular_units_2nd_sem_grade',
                scale=alt.Scale(domain=[df_scatter['Curricular_units_2nd_sem_grade'].min(),
                                        df_scatter['Curricular_units_2nd_sem_grade'].max()])),
        color=alt.Color(field='Status', type='nominal', 
                        scale=alt.Scale(domain=status_counts['Status'].values, 
                        range=['#2FF3E0','#F51720']), legend=None)
    ).interactive()
    st.altair_chart(chart, use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        chart = alt.Chart(df).mark_boxplot(extent='min-max').encode(
            x=alt.X('Admission_grade').scale(zero=False),
            y='Status',
            color=alt.Color(field='Status', type='nominal', 
                        scale=alt.Scale(domain=status_counts['Status'].values, 
                        range=['#2FF3E0','#F51720']), legend=None),
            stroke=alt.value('white')
        )
        st.altair_chart(chart, use_container_width=True, theme='streamlit')
    
    with col2:
        chart = alt.Chart(df).mark_boxplot(extent='min-max').encode(
            x=alt.X('Age_at_enrollment').scale(zero=False),
            y=alt.Y('Status').axis(title=None),
            color=alt.Color(field='Status', type='nominal', 
                        scale=alt.Scale(domain=status_counts['Status'].values, 
                        range=['#2FF3E0','#F51720']), legend=None),
            stroke=alt.value('white')
        )
        st.altair_chart(chart, use_container_width=True, theme='streamlit')


elif selected == 'Predict':

    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("asset\predict_white.png", width=130)
    with col2:
        st.title('Student Dropout Prediction')
        st.header('(Prototype)')

    data = pd.DataFrame()

    # General
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> General </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Age_at_enrollment = float(st.number_input(label='Age_at_enrollment', value=19))
        data["Age_at_enrollment"] = [Age_at_enrollment]
    with col2:
        Gender = st.selectbox(label='Gender', options=dp.encoder_Gender.classes_, index=0)
        data["Gender"] = [Gender]
    with col3:
        Marital_status = st.selectbox(label='Marital_status', options=dp.encoder_Marital_status.classes_, index=3)
        data["Marital_status"] = [Marital_status]
    col1, col2, col3 = st.columns(3)
    with col1:
        International = st.selectbox(label='International', options=dp.encoder_International.classes_, index=0)
        data["International"] = [International]
    with col2:
        Nacionality = st.selectbox(label='Nacionality', options=dp.encoder_Nacionality.classes_, index=2)
        data["Nacionality"] = Nacionality
    # with col3:

    # Application
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Application </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Course = st.selectbox(label='Course', options=dp.encoder_Course.classes_, index=14)
        data["Course"] = Course
    with col2:
        Application_order = int(st.number_input(label='Application_order', value=1))
        data["Application_order"] = Application_order 
    with col3:
        Daytime_evening_attendance = st.selectbox(label='Daytime_evening_attendance', options=dp.encoder_Daytime_evening_attendance.classes_, index=0)
        data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
    col1, col2 = st.columns(2)
    with col1:
        Application_mode = st.selectbox(label='Application_mode', options=dp.encoder_Application_mode.classes_, index=7)
        data["Application_mode"] = [Application_mode]
    with col2:
        Admission_grade = int(st.number_input(label='Admission_grade', value=142.5))
        data["Admission_grade"] = Admission_grade
    col1, col2 = st.columns(2)
    with col1:
        Previous_qualification = st.selectbox(label='Previous_qualification', options=dp.encoder_Previous_qualification.classes_, index=8)
        data["Previous_qualification"] = [Previous_qualification]
    with col2:
        Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=160.0))
        data["Previous_qualification_grade"] = Previous_qualification_grade

    # Additional
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Additional </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=dp.encoder_Tuition_fees_up_to_date.classes_, index=1)
        data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
    with col2:
        Debtor = st.selectbox(label='Debtor', options=dp.encoder_Debtor.classes_, index=0)
        data["Debtor"] = [Debtor]
    with col3:
        Scholarship_holder = st.selectbox(label='Scholarship_holder', options=dp.encoder_Scholarship_holder.classes_, index=1)
        data["Scholarship_holder"] = [Scholarship_holder]  
    col1, col2, col3 = st.columns(3)
    with col1:
        Displaced = st.selectbox(label='Displaced', options=dp.encoder_Displaced.classes_, index=1)
        data["Displaced"] = [Displaced]  
    with col2:
        Educational_special_needs = st.selectbox(label='Educational_special_needs', options=dp.encoder_Educational_special_needs.classes_, index=0)
        data["Educational_special_needs"] = Educational_special_needs
    # with col3:

    # Parents
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Parents </span>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        Fathers_occupation = st.selectbox(label='Fathers_occupation', options=dp.encoder_Fathers_occupation.classes_, index=5)
        data["Fathers_occupation"] = [Fathers_occupation]
    with col2:
        Fathers_qualification = st.selectbox(label='Fathers_qualification', options=dp.encoder_Fathers_qualification.classes_, index=4)
        data["Fathers_qualification"] = [Fathers_qualification]
    col1, col2 = st.columns(2)
    with col1:
        Mothers_occupation = st.selectbox(label='Mothers_occupation', options=dp.encoder_Mothers_occupation.classes_, index=4)
        data["Mothers_occupation"] = Mothers_occupation
    with col2:
        Mothers_qualification = st.selectbox(label='Mothers_qualification', options=dp.encoder_Mothers_qualification.classes_, index=8)
        data["Mothers_qualification"] = [Mothers_qualification]

    # Demographic
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Demographic </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Unemployment_rate = int(st.number_input(label='Unemployment_rate', value=13.9))
        data["Unemployment_rate"] = Unemployment_rate 
    with col2:
        Inflation_rate = int(st.number_input(label='Inflation_rate', value=-0.3))
        data["Inflation_rate"] = Inflation_rate
    with col3:
        GDP = int(st.number_input(label='GDP', value=0.79))
        data["GDP"] = GDP

    # Curricular units 1st sem
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Curricular units 1st sem </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Curricular_units_1st_sem_credited = int(st.number_input(label='1st Credited', value=0))
        data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited 
    with col2:
        Curricular_units_1st_sem_enrolled = int(st.number_input(label='1st Enrolled', value=6))
        data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
    with col3:
        Curricular_units_1st_sem_evaluations = int(st.number_input(label='1st Evaluations', value=6))
        data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations
    col1, col2, col3 = st.columns(3)
    with col1:
        Curricular_units_1st_sem_approved = float(st.number_input(label='1st Approved', value=6))
        data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved 
    with col2:
        Curricular_units_1st_sem_grade = int(st.number_input(label='1st Grade', value=14.0))
        data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade
    with col3:
        Curricular_units_1st_sem_without_evaluations = float(st.number_input(label='1st Without_evaluations', value=0))
        data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations 

    # Curricular units 2nd sem
    st.markdown("---")
    st.markdown("<span style='color:#2FF3E0; font-size:24px'> Curricular units 2nd sem </span>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Curricular_units_2nd_sem_credited = int(st.number_input(label='2nd Credited', value=0))
        data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited 
    with col2:
        Curricular_units_2nd_sem_enrolled = int(st.number_input(label='2nd Enrolled', value=6))
        data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
    with col3:
        Curricular_units_2nd_sem_evaluations = int(st.number_input(label='2nd Evaluations', value=6))
        data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations
    col1, col2, col3 = st.columns(3)
    with col1:
        Curricular_units_2nd_sem_approved = float(st.number_input(label='2nd Approved', value=6))
        data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved
    with col2:
        Curricular_units_2nd_sem_grade = int(st.number_input(label='2nd Grade', value=13.67))
        data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade
    with col3:
        Curricular_units_2nd_sem_without_evaluations = float(st.number_input(label='2nd Without_evaluations', value=0))
        data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations

    with st.expander("View the Raw Data"):
        st.dataframe(data=data, width=800, height=10)

    if st.button('Predict'):
        new_data = dp.data_preprocessing(data=data)
        with st.expander("View the Preprocessed Data"):
            st.dataframe(data=new_data, width=800, height=10)
        st.write("Dropout Status: {}".format(prediction(new_data)))
 
st.caption('Tio Syaifuddin: IDCamp - Data science (expert class)')