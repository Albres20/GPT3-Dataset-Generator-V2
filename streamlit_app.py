# ----------------------Importing libraries----------------------

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.express import colors

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

# tabMain, tabInfo, tabTo_dos = st.tabs(["Main", "Info", "To-do's"])


with st.sidebar:
    image_reddit = st.sidebar.image(
        "Reddit_Thumbnail.jpg",
    )

    input_search = st.sidebar.text_input(
        "Ingrese su palabra de busqueda de reddit", type="default", placeholder="palabra clave"
    )

    image_arrow = st.sidebar.image(
        "Gifs/blue_grey_arrow.gif",
    )

col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.header("Resultados")

    # Columna 1 con tarjetas scrollables
    for i in range(50):
        with col1:
            st.markdown(f"""
            <style>
              .card {{
                background-color: #fff;
                border-radius: 4px;
                border: 1px solid #e5e5e5;  
                margin-bottom: 15px;
              }}
              .card-title {{
                font-size: 16px;
                font-weight: 600;  
              }} 
              .card-text {{
                color: #878787;
              }}
            </style>

            <div class="card">
              <div class="row">
                <div class="col-2">
                   <img src="https://cdn3.iconfinder.com/data/icons/2018-social-media-logotypes/1000/2018_social_media_popular_app_logo_reddit-512.png" class="img-fluid rounded-circle" width="40">
                </div>
                <div class="col-10">
                  <div class="row">
                     <h6 class="card-title">Usuario {i}</h6>
                     <p class="card-text">
                       Preview del contenido aquí
                     </p>
                  </div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            # CSS para permitir scroll
    # col1.markdown("""
    # <style>
    # .element-container {
    #    max-height: 300px;
    #    overflow-y: auto;
    # }
    # </style>
    # """, unsafe_allow_html=True)

with col2:
    st.header("Graficos de analisis")

    # Gráfico 1
    values = [20, 20, 30]
    fig = go.Figure(data=[go.Pie(labels=['A', 'B', 'C'],
                                 values=values,
                                 hole=.4,
                                 sort=False)])
    fig.update_traces(hoverinfo='label+value')
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig.update_layout(width=500, height=300)

    col2.plotly_chart(fig)

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

    col2.plotly_chart(fig)


st.write("")
