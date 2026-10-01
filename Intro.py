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
 st.write("Aplicación basada en algoritmos vectorizados con NumPy y análisis de complejidad operacional para monitorear flujos de datos continuos."
 " Identifica comportamientos atípicos o fallas críticas en tiempo real dentro de grandes cantidades de datos, reduciendo falsos positivos e interviniendo antes de que ocurra una falla en el sistema.") 
 url = "https://detectoranomalias-24iapppjcyvsnzyluoulm4u.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Fertilidad en Agrosavia")
 image = Image.open('agrosavia.jpg')
 st.image(image, use_container_width=True)
 st.write(" Modelo de clasificación KNN aplicado a las características físico-químicas del suelo agronómico colombiano."
 " Determina la fertilidad y aptitud del suelo de forma instantánea, ayudando a los agricultores a tomar decisiones informadas sobre cultivos e insumos agrícolas.") 
 url = "https://fertilidad-ymzy8pr87tbzjzhwtxoquh.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Regresión viviendas en California")
 image = Image.open('regresion_viviendas.jpg')
 st.image(image, use_container_width=True)
 st.write("Modelo estadístico y predictivo basado en el conjunto de datos de viviendas en California."
 " Estima el valor comercial de propiedades en función de variables socioeconómicas y geográficas, facilitando la valoración inmobiliaria.") 
 url = "https://gradiente-pvblfgce3s8jam2jxarzvw.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

with col2: 
 st.subheader("Nivel de ríos")
 image = Image.open('nivel_rios.jpg')
 st.image(image, use_container_width=True)
 st.write("Sistema de análisis hídrico orientado a la supervisión ambiental de CORNARE en cauces principales del oriente Antioqueño."
 " Previene emergencias e inundaciones mediante el monitoreo continuo de los niveles de agua, emitiendo alertas tempranas para las comunidades y entes de control.") 
 url = "https://lluviacornare-f8ywcsnh7eimdtd2wngtww.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Nivel de quebrada")
 image = Image.open('nivel_quebradas.jpg')
 st.image(image, use_container_width=True)
 st.write("Aplicación enfocada en la microcuenca específica de la quebrada La Honda en el municipio de Guarne."
 " Proporciona un seguimiento focalizado de los niveles del agua local frente a eventos de lluvia severa, mitigando riesgos de desbordamiento en zonas habitadas.") 
 url = "https://lluviacornare-jdlrhhk6dvlmpsfpzuwtyw.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Predictor de sensación térmica")
 image = Image.open('predictor_termico.jpg')
 st.image(image, use_container_width=True)
 st.write("Algoritmo que calcula la temperatura percibida combinando datos en tiempo real de temperatura ambiental y humedad relativa."
 " Evalúa condiciones térmicas para la salud humana.") 
 url = "https://predictorsensatermica-uyirhmlekubzthq6hmnmge.streamlit.app"
 st.write(f"Link: [Enlace]({url})")


with col3: 
 st.subheader("Predictor de calidad del aire")
 image = Image.open('calidad_aire.jpg')
 st.image(image, use_container_width=True)
 st.write("Herramienta analítica que procesa mediciones de material particulado y gases contaminantes bajo la metodología del marco ambiental de CORNARE."
 " Pronostica la concentración de contaminantes atmosféricos para planificar medidas de mitigación y proteger la salud pública regional.") 
 url = "https://pronosticocornare-2re6csyn5vm7vxjyvm4lbd.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Descenso de gradiente")
 image = Image.open('descenso_gradiente.jpg')
 st.image(image, use_container_width=True)
 st.write("Visualizador matemático paso a paso del algoritmo fundamental de optimización utilizado en el entrenamiento de redes neuronales y regresiones."
 " Permite comprender la convergencia de modelos, facilitando el ajuste eficiente de parámetros y la reducción del error de entrenamiento.") 
 url = "https://ygvrolltj4wb5flx5tq7t5.streamlit.app"
 st.write(f"Link: [Enlace]({url})")
 
 st.subheader("Predictor de lluvia")
 image = Image.open('predictor_lluvia.jpg')
 st.image(image, use_container_width=True)
 st.write("Modelo probabilístico que analiza variables meteorológicas como presión, humedad, viento para estimar la probabilidad de lluvia."
 " Ayuda en la planificación logística, agrícola y urbana al predecir eventos de lluvia para el día siguiente con un porcentaje de certeza cuantificable.") 
 url = "https://regresionlogistica-uvkgnjnnow96mbafsxfvq2.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

with col4:
 st.subheader("Series de tiempo")
 image = Image.open('series_tiempo.jpg')
 st.image(image, use_container_width=True)
 st.write("Plataforma de análisis temporal conectada a sensores físicos que capturan lecturas de temperatura de manera continua."
 " Identifica patrones, estacionalidades y tendencias térmicas en entornos industriales o ambientales para preveer comportamientos futuros y optimizar recursos.") 
 url = "https://seriestiempo-hcftvunhnv7gxbdfbmqryv.streamlit.app"
 st.write(f"Link: [Enlace]({url})")

 st.subheader("Sensores IoT de temperatura")
 image = Image.open('preparacion_datos.jpg')
 st.image(image, use_container_width=True)
 st.write("Herramienta interactiva enfocada en las etapas de limpieza, transformación, imputación y estructuración de conjuntos de datos crudos."
 " Elimina el ruido, inconsistencias y datos faltantes antes del modelado, garantizando que los algoritmos de machine learning trabajen con información y datos confiables.") 
 url = "https://temperatura-dm8dmwqydjomzryarucixh.streamlit.app"
 st.write(f"Link: [Enlace]({url})")
