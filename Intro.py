import streamlit as st
from PIL import Image
st.title("Aplicaciones de IoT y machine learning")

st.markdown("""
<style>

    /* Contenedor principal */
    .block-container {
        max-width: 1400px;
        padding-top: 2rem;
        padding-bottom: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    /* Título principal */
    h1 {
        text-align: center;
        margin-bottom: 10px;
    }

    /* Texto introductorio */
    .intro {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    /* Imágenes */
    img {
        border-radius: 10px;
    }

    /* Espacio entre columnas */
    [data-testid="column"] {
        padding: 10px;
    }

</style>
""", unsafe_allow_html=True)

with st.sidebar:
  st.subheader("Portafolio Samuel")
  parrafo = (
    "Este portafolio reúne un conjunto de aplicaciones interactivas y modelos matemáticos aplicados a la resolución de problemas reales, realizadas en el curso de programación avanzada."
    " A través del análisis de datos, Machine Learning e Internet de las Cosas (IoT), estas herramientas permiten optimizar procesos agrícolas,"
    "monitorear variables ambientales en tiempo real, predecir tendencias clave y transformar datos complejos en decisiones automatizadas y eficientes."
  )
  st.write(parrafo)


st.write(f"Aplicaciones:")
col1, col2, col3, col4 = st.columns(4, gap="large")

with col1:
 
 st.subheader("Detector de anomalías")
 image = Image.open('detector_anomalias.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://detectoranomalias-24iapppjcyvsnzyluoulm4u.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Fertilidad en Agrosavia")
 image = Image.open('agrosavia.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://fertilidad-ymzy8pr87tbzjzhwtxoquh.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Regresión viviendas en California")
 image = Image.open('regresion_viviendas.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://gradiente-pvblfgce3s8jam2jxarzvw.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

with col2: 
 st.subheader("Nivel de ríos")
 image = Image.open('nivel_rios.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://lluviacornare-f8ywcsnh7eimdtd2wngtww.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Nivel de quebrada")
 image = Image.open('nivel_quebradas.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://lluviacornare-jdlrhhk6dvlmpsfpzuwtyw.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Predictor de sensación térmica")
 image = Image.open('predictor_termico.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://predictorsensatermica-uyirhmlekubzthq6hmnmge.streamlit.app"
 st.write(f"Link: [Enlace]({url})")


with col3: 
 st.subheader("Predictor de calidad del aire")
 image = Image.open('calidad_aire.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://pronosticocornare-2re6csyn5vm7vxjyvm4lbd.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Descenso de gradiente")
 image = Image.open('descenso_gradiente.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://ygvrolltj4wb5flx5tq7t5.streamlit.app"
 st.write(f"Link: [Enlace]({url})")
 
 st.subheader("Predictor de lluvia")
 image = Image.open('predictor_lluvia.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://regresionlogistica-uvkgnjnnow96mbafsxfvq2.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

with col4:
 st.subheader("Series de tiempo")
 image = Image.open('series_tiempo.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://seriestiempo-hcftvunhnv7gxbdfbmqryv.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Sensores IoT de temperatura")
 image = Image.open('preparacion_datos.jpg')
 st.image(image, use_container_width=True)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://temperatura-dm8dmwqydjomzryarucixh.streamlit.app"
 st.write(f"Link: [Enlace]({url})")
