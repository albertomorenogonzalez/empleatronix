import streamlit as st
import pandas as pd
import numpy as np

st.title('EMPLEATRONIX')
st.subheader('Todos los datos sobre los empleados en una aplicación.')

@st.cache_data
def load_data():
    data = pd.read_csv('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    return data

data = load_data()

if st.checkbox('Mostrar datos de empleados'):
    st.subheader('Datos de los Empleados')
    st.write(data)