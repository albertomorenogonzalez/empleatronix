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
    show_name = st.toggle('Mostrar el nombre')

with col3:
    show_salary = st.toggle('Mostrar el sueldo en la barra')


fig, ax = plt.subplots()

# Create a new DataFrame based on visibility settings
visible_data = data[['full name', 'salary']] if show_name and show_salary else data[['empty', 'salary']]

if show_name:
    ax.barh(visible_data['full name'], visible_data['salary'], color=color)
else:
    ax.barh(visible_data['empty'], visible_data['salary'], color=color)

# Set labels and title
ax.set_xlabel('Salary')
ax.set_ylabel('Full Name' if show_name else '')
ax.set_title('Horizontal Bar Chart')

# Display the plot using Streamlit
st.pyplot(fig)
