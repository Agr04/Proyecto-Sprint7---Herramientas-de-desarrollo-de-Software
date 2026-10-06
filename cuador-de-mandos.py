import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.title('Graficas de distacnia recorrida por vehiculos / Odometro')

car_data = pd.read_csv('vehicles_us.csv')

# Crear botonde historial

hist_button = st.button('Construir histograma')

build_table = st.checkbox('Mostrar promedio de kilometraje en top 5 Modelos')

if build_table:
    st.write('Kilometraje promedio para Top 5 modelos')

    lista_modelos = car_data['model'].value_counts().head()
    modelos = lista_modelos.index

    odometer_mean = car_data.groupby('model')['odometer'].mean()
    odometer_meanT5 = odometer_mean.loc[modelos]

    st.dataframe(odometer_meanT5)


if hist_button:
    st.write(
        'Creación de un histograma para conjunto de datos de anuncios de venta de coches')

    # Crear histograma utilizando plotly.graph objects
    # Se crea figura vacia y luego rastro del histoframa

    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro',
                      xaxis_title='Odomter values', yaxis_title='Frequency')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir Scatter plot')

if scatter_button:
    st.write(
        'Creación de un Scatter plot / dispercion para conjunto de datos de anuncios de venta de coches')

    fig2 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig2.update_layout(title_text='Relación entre Odómetro y Precio',
                       xaxis_title='odometer value', yaxis_title='price')

    st.plotly_chart(fig2, use_container_width=True)

build_table2 = st.checkbox('tabla de 5 modelos mas costosos')

if build_table2:
    st.dataframe(car_data.groupby('model')[
                 'price'].mean().sort_values(ascending=False).head())
