import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.express import colors
import os


CSV_DIR = 'csv_uploads'
# ----------------------Page config--------------------------------------
st.set_page_config(page_title="Analisis de sentimiento de Reddit", page_icon="📩", layout="wide")

# layout="centered"

# ----------------------Sidebar section--------------------------------
c30, c31, c32 = st.columns([0.2, 0.1, 3])

with c30:
    st.caption("")

    st.image("reddit_icon.png", width=60)

with c32:
    st.title("Resultados de busqueda en reddit")

st.write(
    "Los resultados mostrados son generados en base a la palabra clave en reddit, el cual puede ser cambiada en el menu lateral. "
)

# Importa streamlit
import streamlit as st

# Carga el archivo CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Llama a la función para cargar el archivo CSSs
local_css("styles.css")

with st.sidebar:
    image_reddit = st.sidebar.image(
        "Reddit_Thumbnail.jpg",
    )

    input_search = st.sidebar.text_input(
        "Ingrese su palabra de búsqueda de Reddit (máx. 15 caracteres)",
        max_chars=15,
        placeholder="palabra clave"
    )

    if st.sidebar.checkbox('Cargar archivo CSV externo'):
        if not os.path.exists(CSV_DIR):
            os.mkdir(CSV_DIR)

        uploaded_file = st.file_uploader("Elige un archivo CSV", type=['csv'], accept_multiple_files=False)

        if uploaded_file:

            csv_path = os.path.join(CSV_DIR, uploaded_file.name)

            if os.path.isfile(csv_path):
                st.warning(f"El archivo {uploaded_file.name} ya existe y será sobreescrito")

            # Guardar archivo
            with open(csv_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())
            st.success("Archivo guardado exitosamente!")

image_arrow = st.sidebar.image(
    "Gifs/blue_grey_arrow.gif",
)

# Función para cargar más resultados
def cargar_mas_resultados():
    st.session_state["num_resultados"] += 10

# Inicializar la variable de estado
if "num_resultados" not in st.session_state:
    st.session_state["num_resultados"] = 10

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.header("Resultados")

    # Columna 1 con tarjetas scrollables
    for i in range(st.session_state["num_resultados"]):
        st.markdown(f"""
        <div class="card">
          <div class="user-info">
            <img src="https://cdn3.iconfinder.com/data/icons/2018-social-media-logotypes/1000/2018_social_media_popular_app_logo_reddit-512.png" class="img-fluid rounded-circle" width="40">
            <h6 class="card-title">Usuario {i}</h6>
          </div>
          <div>
            <p class="card-text">
              Preview del contenido aquí
            </p>
          </div>
        </div>
        """, unsafe_allow_html=True)

    # Botón para cargar más resultados
    if st.button("Cargar más resultados"):
        cargar_mas_resultados()

with col2:
    st.header("Gráficos de análisis")

    # Estilo CSS para fijar la posición
    st.markdown(
        """
        <style>
        .col2-container {
            position: sticky !important;
            top: 0 !important;
            z-index: 1 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Contenedor para los gráficos
    st.markdown('<div class="col2-container">', unsafe_allow_html=True)

    # Gráfico 1
    values = [20, 20, 30]
    fig = go.Figure(data=[go.Pie(labels=['A', 'B', 'C'],
                                 values=values,
                                 hole=.4,
                                 sort=False)])
    fig.update_traces(hoverinfo='label+value')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_layout(width=500, height=300)
    st.plotly_chart(fig)

    # Gráfico 3D en columna 2
    values = [10, 20, 50]
    fig = go.Figure(data=[go.Pie(labels=['A', 'B', 'C'],
                                 values=values,
                                 hole=.4,
                                 marker=dict(colors=colors.qualitative.Dark24),
                                 sort=False)])
    fig.update_traces(hoverinfo='label+value')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_layout(width=500, height=300)
    st.plotly_chart(fig)

    # Cierre del contenedor
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
