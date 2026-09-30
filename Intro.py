import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Aplicaciones con Inteligencia Artificial.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Detector de anomalías")
 image = Image.open('detector_anomalias.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://detectoranomalias-24iapppjcyvsnzyluoulm4u.streamlit.app"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader("Fertilidad en Agrosavia")
 image = Image.open('agrosavia.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://fertilidad-ymzy8pr87tbzjzhwtxoquh.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Regresión viviendas en California")
 image = Image.open('regresion_viviendas.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://gradiente-pvblfgce3s8jam2jxarzvw.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Nivel de ríos")
 image = Image.open('nivel_rios.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://lluviacornare-f8ywcsnh7eimdtd2wngtww.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Nivel de quebrada")
 image = Image.open('nivel_quebradas.jpg')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://lluviacornare-jdlrhhk6dvlmpsfpzuwtyw.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Predictor de sensación térmica")
 image = Image.open('predictor_termico.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://predictorsensatermica-uyirhmlekubzthq6hmnmge.streamlit.app"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Predictor de calidad del aire")
 image = Image.open('calidad_aire.jpg')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://pronosticocornare-2re6csyn5vm7vxjyvm4lbd.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Descenso de gradiente")
 image = Image.open('descenso_gradiente.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://ygvrolltj4wb5flx5tq7t5.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Predictor de lluvia")
 image = Image.open('predictor_lluvia.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://regresionlogistica-uvkgnjnnow96mbafsxfvq2.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

with col4
 st.subheader("Series de tiempo")
 image = Image.open('series_tiempo.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://seriestiempo-hcftvunhnv7gxbdfbmqryv.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

 st.subheader("Sensores IoT de temperatura")
 image = Image.open('preparacion_datos.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://temperatura-dm8dmwqydjomzryarucixh.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
