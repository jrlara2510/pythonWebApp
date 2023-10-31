#streamlit run app.py

import pandas as pd
import plotly.express as px
import streamlit as st

# Lectura y tratamiento de los datos
car_data = pd.read_csv('vehicles_us.csv') 
# Transformación de fecha de publicación
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])
car_data['year_posted'] = car_data['date_posted'].dt.year
car_data['years_old'] = car_data['date_posted'].dt.year - car_data.model_year

# Set the title or header for your Streamlit app
st.title("Distribución de datos de dataset de venta de vehiculos")

#Descripcion
st.markdown(""" \n Analisis Exploratorio de datos para el dataset **vehicules_us.csv**, el cual contiene información sobre la venta de un vehículo, y los diversos factores que llegan a fectar en el precio de este. Algunos de ellos son el modelo del vehiculo, el estado, año, millaje recorrido, color, entre otros.  \n""")

# Create a layout with two columns
col1, col2, col3 = st.columns(3)

# Add check buttons to the columns
check_box_hist = col1.checkbox("Genera Histograma")
check_box_disp = col2.checkbox("Genera Grafico de Dispersión")
check_scatter_matrix = col3.checkbox("Genera grafico de correlaciones.")

if check_box_hist: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para la distribución del millaje de vehiculos.')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 
    

if check_box_disp: # al hacer clic en el botón   
    # escribir un mensaje
    st.write('Creación de un grafico de dispersión de millaje contra precio del vehiculo.')
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 

if check_scatter_matrix: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de correlacion del precio del vehiculo cotra los años y el millaje.')
    columns = ['price','years_old','odometer']

    fig = px.scatter_matrix(car_data, dimensions=columns, title='Precio del vehiculo vs año & millaje.')
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 