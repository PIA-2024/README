import streamlit as st

st.header('Lanzar una moneda')

st.write('Esta aplicación aún no es funcional. En construcción.')

import pandas as pd
import plotly.express as px

car_data = pd.read_csv('DATASETS/vehicles_us.csv') # leer los datos
fig = px.histogram(car_data, x="odometer") # crear un histograma
fig.show() # crear gráfico de dispersión

import pandas as pd
import plotly.express as px

car_data = pd.read_csv('DATASETS/vehicles_us.csv') # leer los datos
fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
fig.show() # crear gráfico de dispersión
