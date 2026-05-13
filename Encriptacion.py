import streamlit as st
import numpy as np

# Configuración de página
st.set_page_config(page_title="UDES - Cifrado Matricial", layout="wide")
st.title("🔐 Sistema de Cifrado con Botones de Copiado")
st.markdown("### Proyecto de Aula - Álgebra Lineal (UDES)")

# --- PANEL LATERAL ---
st.sidebar.header("⚙️ Configuración")
dimension = st.sidebar.select_slider("Dimensión de la matriz", options=[2, 3, 4], value=2)

# Inicializar matriz clave en la sesión
if 'K' not in st.session_state or st.session_state.K.shape[0] != dimension:
    st.session_state.K = np.eye(dimension)

if st.sidebar.button("Generar Nueva Matriz Clave"):
    while True:
        nueva_K = np.random.randint(1, 10, (dimension, dimension))
        # Verificación de invertibilidad
        if abs(np.linalg.det(nueva_K)) > 0.1:
            st.session_state.K = nueva_K
            break
    st.sidebar.success("¡Clave Generada!")

st.sidebar.write("Matriz Clave (K):")
st.sidebar.write(st.session_state.K)

# --- SECCIÓN 1: ENCRIPTADOR ---
st.header("1. 📝 Encriptación")
mensaje_input = st.text_input("Escribe el mensaje para encriptar:")

if mensaje_input:
    n = dimension
    # Conversión de texto a valores ASCII
    nums = [ord(c) for c in mensaje_input]
    # Relleno (Padding) con ceros para completar la matriz
    while len(nums) % n != 0:
        nums.append(0)
    
    M = np.array(nums).reshape(n, -1)
    # Operación fundamental: C = K * M
    C = np.dot(st.session_state.K, M)
    # Cálculo de la inversa K⁻¹
    K_inv = np.linalg.inv(st.session_state.K)

    # Formateo de strings para copiado rápido (sin corchetes)
    c_str = " ".join(map(str, C.flatten()))
    inv_str = " ".join(map(str, np.round(K_inv, 4).flatten()))

    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Matriz Cifrada (C)")
        st.write(C)
        st.code(c_str, language=None)
        st.caption("Copia estos números usando el icono en la esquina del cuadro negro.")
    
    with col2:
        st.subheader("Matriz Inversa (K⁻¹)")
        st.write(np.round(K_inv, 4))
        st.code(inv_str, language=None)
        st.info("💡 Copia esta matriz para usarla en el decodificador de abajo.")

st.divider()

# --- SECCIÓN 2: DECODIFICADOR INDEPENDIENTE ---
st.header("2. 🔓 Decodificador Manual")
st.write("Pega los datos aquí para demostrar la recuperación de información:")
col_a, col_b = st.columns(2)

with col_a:
    msj_cifrado_raw = st.text_area("Pega aquí los números de la Matriz C:")

with col_b:
    inversa_raw = st.text_area("Pega aquí los números de la Matriz Inversa:")

if st.button("🚀 Descifrar Ahora"):
    if msj_cifrado_raw and inversa_raw:
        try:
            # Procesamiento de las entradas de texto
            c_nums = np.fromstring(msj_cifrado_raw.replace(',', ' '), sep=' ')
            inv_nums = np.fromstring(inversa_raw.replace(',', ' '), sep=' ')
            
            # Reconstrucción de las formas matriciales
            matriz_C_ext = c_nums.reshape(dimension, -1)
            matriz_Inv_ext = inv_nums.reshape(dimension, dimension)
            
            # Operación de recuperación: M = K⁻¹ * C
            M_rec = np.dot(matriz_Inv_ext, matriz_C_ext)
            
            # REDONDEO CRÍTICO: Elimina errores de precisión decimal
            nums_final = np.round(M_rec).flatten().astype(int)
            
            # Traducción de números a caracteres, ignorando el relleno (ceros)
            texto_descifrado = "".join([chr(i) for i in nums_final if i > 0])
            st.success(f"✅ Mensaje recuperado: **{texto_descifrado}**")
        except Exception as e:
            st.error("Error: Asegúrate de que los números correspondan a la dimensión seleccionada.")
    else:
        st.warning("Debes completar ambos campos para descifrar.")