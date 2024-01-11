import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('EMPLEATRONIX')
st.subheader('Todos los datos sobre los empleados en una aplicación.')

@st.cache_data
def load_data():
    data = pd.read_csv('data/employees.csv')
    return data

data = load_data()

if st.checkbox('Mostrar datos de empleados'):
    st.subheader('Datos de los Empleados')
    st.write(data)
