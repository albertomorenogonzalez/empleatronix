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

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker('Elige un color para las barras', '#3475B3')

with col2:
    name = st.toggle('Mostrar el nombre')

with col3:
    salary = st.toggle('Mostrar el sueldo en la barra')


fig, ax = plt.subplots()

bars = ax.barh(data['full name'], data['salary'], color=color)

def show_name(name, bars):
    if not name:
        ax.yaxis.set_visible(False)
        ax.set_ylim([-0.5, len(data['full name']) - 0.5])

    show_salary(salary, bars)

def show_salary(salary, bars):
    if salary:
        ax.bar_label(bars, padding=5)

show_name(name, bars)

st.pyplot(fig)
