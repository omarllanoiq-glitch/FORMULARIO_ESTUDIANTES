import streamlit as st
import requests
from PIL import Image

# --- CONFIGURACIÓN DE PÁGINA ---
# Esto debe ser lo PRIMERO en el código. Configura el título de la pestaña del navegador y el ícono.
st.set_page_config(
    page_title="Registro SENATI",
    page_icon="⚙️",
    layout="centered"
)

# --- TU URL DE APPS SCRIPT ---
# ¡NO OLVIDES PEGAR TU URL AQUÍ!
URL_APPS_SCRIPT = "TU_URL_ORIGINAL_AQUI"

# --- ENCABEZADO ESTILO INSTITUCIONAL (Con un truco de HTML/CSS) ---
# Esto crea una barra azul superior para darle identidad
st.markdown("""
    <div style='background-color:#003366; padding:20px; border-radius:10px; margin-bottom:25px; text-align:center'>
        <h2 style='color:white; margin:0; font-weight: 700;'>🏭 Centro de Formación Técnica</h2>
        <p style='color:#e0e0e0; margin:5px; font-size: 1.1rem;'>Portal de Registro de Estudiantes</p>
    </div>
""", unsafe_allow_html=True)


# --- INTRODUCCIÓN ---
st.write("Bienvenido. Por favor, completa el siguiente formulario técnico con tus datos académicos.")
st.markdown("---") # Una línea separadora sutil

# --- FORMULARIO CON MEJOR DISEÑO ---
with st.form("mi_formulario_senati"):
    # Usamos columnas para organizar los campos en una misma fila
    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input("👤 Nombre Completo", placeholder="Ej: Juan Pérez")
    with col2:
        correo = st.text_input("📧 Correo Institucional", placeholder="Ej: jperez@senati.pe")

    # Selector de curso con íconos
    curso = st.selectbox(
        "🛠️ Selecciona tu Especialidad/Curso:",
        [
            "Mecánica Automotriz",
            "Electrotecnia Industrial",
            "Desarrollo de Software",
            "Control de Procesos Industriales",
            "Administración Industrial",
            "Otro"
        ]
    )
    
    respuesta = st.text_area("📝 Comentarios Adicionales o Consultas Técnicas", height=100)
    
    # Espacio para empujar el botón un poco abajo
    st.write("")
    
    # El botón de envío (tomará el color azul del tema que definiremos luego)
    # Usamos use_container_width=True para que el botón ocupe todo el ancho y se vea fuerte
    submitted = st.form_submit_button("ENVIAR REGISTRO 🚀", use_container_width=True)

    if submitted:
        if not nombre or not correo:
            st.warning("⚠️ Por favor, completa los campos obligatorios (Nombre y Correo).")
        else:
            # Datos a enviar
            datos = {
                "nombre": nombre,
                "correo": correo,
                "curso": curso,
                "respuesta": respuesta
            }
            
            # Spinner de carga visual mientras envía
            with st.spinner("Procesando envío al servidor..."):
                try:
                    r = requests.post(URL_APPS_SCRIPT, json=datos)
                    if r.status_code == 200:
                        # Mensaje de éxito en verde, grande y claro
                        st.balloons()
                        st.success(f"✅ ¡Registro Exitoso! Tus datos para la especialidad de **{curso}** han sido guardados correctamente en el sistema.")
                    else:
                        st.error("❌ Error en el servidor. Intente nuevamente.")
                except:
                    st.error("📡 Error de conexión. Verifique su internet.")

# Pie de página sutil
st.markdown("---")
st.caption("© 2024 - Sistema de Registro Académico - Uso Interno")
