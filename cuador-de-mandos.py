import pandas as pd
import plotly.graph_objects as go
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# Crear botonde historial

hist_button = st.button('Construir histograma')

if hist_button:
    st.write(
        'Creación de un histograma para conjunto de datos de anuncios de venta de coches')

    # Crear histograma utilizando plotly.graph objects
    # Se crea figura vacia y luego rastro del histoframa

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir Scatter plot')

if scatter_button:
    st.write(
        'Creación de un Scatter plot / dispercion para conjunto de datos de anuncios de venta de coches')

    fig2 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig2.update_layout(title_text='Relación entre Odómetro y Precio')

    st.plotly_chart(fig2, use_container_width=True)
