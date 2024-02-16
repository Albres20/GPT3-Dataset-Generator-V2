from bs4 import BeautifulSoup
import pandas as pd
import requests

def extraer_html(word):
    
    try:
        url_tweet = "https://www.reddit.com/search/?q="+word
        response = requests.get(url_tweet)
        if response.status_code == 200:
            return response.text
        else:
            print("Error al obtener el HTML. Código de estado:", response.status_code)
            return None
    except Exception as e:
        print("Error al realizar la solicitud:", str(e))
        return None
    
def extraer_informacion(html):
    soup = BeautifulSoup(html, 'html.parser')
    temas = []
    subreddits = []
    srcs = []  # Lista para almacenar los srcs
    for enlace in soup.find_all('a', {'data-testid': 'post-title'}):
        href = enlace.get('href')
        if href.startswith('/r/'):
            partes = href.split('/')
            subreddit = partes[2]
            tema = partes[5].replace("_"," ")
            subreddits.append(subreddit)
            temas.append(tema)
            # Buscar el elemento faceplate-img
            faceplate_img = enlace.find_next('faceplate-img')
            if faceplate_img:  # Si se encuentra
                src = faceplate_img.get('src')
  
                srcs.append(src)
            else:  # Si no se encuentra, añadir None
                srcs.append(None)
    return temas, subreddits, srcs  # Devolver también la lista de srcs

#Ingresa la palabra
word="asesinato"
#  Extractor de HTML
html_ejemplo = extraer_html(word)

# Extraer información del HTML de ejemplo
temas, subreddits, srcs = extraer_informacion(html_ejemplo)

# Creando datframe
df = pd.DataFrame({'Subreddit': subreddits, 'Tema': temas, 'Src': srcs})

# Muestreo de dataframe
print(df)

# Generar csv
df.to_csv('datos.csv', index=False)