import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('DATASETS/vehicles_us.csv')  # Asegúrate de que el archivo CSV esté en el mismo directorio que app.py

# Crear un encabezado para la aplicación
st.header('Cuadro de Mandos de Anuncios de Venta de Coches')

# Crear una casilla de verificación para el histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # Si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    
    # Crear un histograma
    fig_hist = px.histogram(car_data, x='odometer')
    
    # Mostrar el histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Crear una casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # Si la casilla de verificación está seleccionada
    st.write('Construir un gráfico de dispersión para las columnas precio y odómetro')
    
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Precio vs Odómetro')
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)