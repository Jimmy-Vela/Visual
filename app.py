import streamlit as st

# Configuración de la página web (Título e icono en la pestaña del navegador)
st.set_page_config(
    page_title="Detector de Polaridad Molecular", 
    page_icon="🧪",
    layout="centered"
)

# Base de datos de las moléculas más comunes y su análisis
moleculas = {
    "Agua (H2O)": {
        "formula": "H₂O",
        "geometria": "Angular",
        "polaridad": "Polar",
        "explicacion": "El oxígeno es mucho más electronegativo que el hidrógeno. Debido a su geometría angular, los vectores de los dipolos no se cancelan, generando un momento dipolar neto positivo."
    },
    "Dióxido de Carbono (CO2)": {
        "formula": "CO₂",
        "geometria": "Lineal",
        "polaridad": "Apolar",
        "explicacion": "Aunque los enlaces Carbono-Oxígeno son polares, la molécula es completamente lineal y simétrica. Los dipolos jalan con la misma fuerza en sentidos opuestos y se cancelan mutuamente."
    },
    "Metano (CH4)": {
        "formula": "CH₄",
        "geometria": "Tetraédrica",
        "polaridad": "Apolar",
        "explicacion": "Es una molécula altamente simétrica. Los pequeños dipolos de los cuatro enlaces C-H se cancelan perfectamente en el espacio tridimensional."
    },
    "Amoníaco (NH3)": {
        "formula": "NH₃",
        "geometria": "Piramidal trigonal",
        "polaridad": "Polar",
        "explicacion": "El Nitrógeno tiene un par de electrones libres que empuja los enlaces N-H hacia abajo. Esto rompe la simetría y concentra la carga negativa en el vértice."
    },
    "Clorometano (CH3Cl)": {
        "formula": "CH₃Cl",
        "geometria": "Tetraédrica (Asimétrica)",
        "polaridad": "Polar",
        "explicacion": "El Cloro atrae los electrones con mucha más fuerza que el Carbono y el Hidrógeno. Al no haber simetría para compensarlo, la molécula se vuelve polar."
    },
    "Oxígeno diatómico (O2)": {
        "formula": "O₂",
        "geometria": "Lineal",
        "polaridad": "Apolar",
        "explicacion": "Al estar formada por dos átomos idénticos, comparten los electrones de manera equitativa. La diferencia de electronegatividad es cero."
    }
}

# --- DISEÑO DE LA INTERFAZ ---
st.title("🧪 Identificador de Polaridad Molecular")
st.write("Selecciona una molécula para evaluar su polaridad basándonos en su **geometría molecular** y **electronegatividad**.")

st.markdown("---")

# Selector de moléculas para el usuario
opcion = st.selectbox("Elige una molécula para analizar:", list(moleculas.keys()))

# Extraer los datos de la molécula seleccionada
datos = moleculas[opcion]

# Mostrar información clave en columnas
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Fórmula Química", value=datos["formula"])
    st.markdown(f"**Geometría Molecular:** {datos['geometria']}")

with col2:
    # Cambia el color de la tarjeta según si es Polar o Apolar
    if datos["polaridad"] == "Polar":
        st.error(f"Resultado: **{datos['polaridad']}** 💧")
    else:
        st.success(f"Resultado: **{datos['polaridad']}** ⛽")

# Sección de explicación teórica para el profesor
st.subheader("🔬 Justificación Química")
st.info(datos["explicacion"])

# Nota técnica elegante al pie de página
st.caption("Criterio: La polaridad depende del momento dipolar neto ($$\\mu$$). Si $$\\mu \\neq 0$$ es Polar; si $$\\mu = 0$$ es Apolar.")