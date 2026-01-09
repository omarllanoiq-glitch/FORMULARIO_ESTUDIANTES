import streamlit as st
import requests

# --- EN TU ARCHIVO app.py ---

# Pega esto justo después de st.set_page_config(...)

hide_elements = """
    <style>
    /* Ocultar menú de hamburguesa (tres rayas) superior derecha */
    #MainMenu {visibility: hidden;}
    
    /* Ocultar pie de página "Made with Streamlit" */
    footer {visibility: hidden;}
    
    /* Ocultar la barra de decoración superior (la línea de colores) */
    header {visibility: hidden;}
    
    /* Ajuste específico para móviles: Ocultar barra superior vacía si queda alguna */
    div[data-testid="stHeader"] {
        visibility: hidden;
        height: 0px;
    }
    </style>
"""
st.markdown(hide_elements, unsafe_allow_html=True)
# -----------------------------------------


# --- 2. TU URL DE APPS SCRIPT ---
# ⚠️ IMPORTANTE: Borra lo de abajo y pega TU URL que termina en /exec
URL_APPS_SCRIPT = "https://script.google.com/macros/s/AKfycbwfkvRYuit-2l79v3wgFJEmMuIRt3_SCbGvuG3c5Z90aUv7snPM2wlrJ4mHiJfEhu1YWw/exec"


# --- 3. ENCABEZADO ESTILO INSTITUCIONAL ---
# Barra azul superior con título
st.markdown("""
    <div style='background-color:#003366; padding:20px; border-radius:10px; margin-bottom:25px; text-align:center'>
        <h2 style='color:white; margin:0; font-family:sans-serif;'>🏭 Centro de Formación Técnica</h2>
        <p style='color:#e0e0e0; margin:5px; font-size: 1.1rem;'>Portal de Registro de Estudiantes</p>
    </div>
""", unsafe_allow_html=True)


# --- 4. FORMULARIO ---
st.write("Bienvenido. Por favor, completa tus datos para el registro del semestre.")

with st.form("mi_formulario_senati"):
    
    # Creamos dos columnas para que Nombre y Correo estén lado a lado
    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input("👤 Nombre Completo", placeholder="Ej: Juan Pérez")
    with col2:
        correo = st.text_input("📧 Correo Institucional", placeholder="Ej: jperez@senati.pe")

    # Selector de especialidad
    curso = st.selectbox(
        "🛠️ Selecciona tu Especialidad:",
        [
            "Mecánica Automotriz",
            "Electrotecnia Industrial",
            "Desarrollo de Software",
            "Control de Procesos Industriales",
            "Administración Industrial",
            "Otro"
        ]
    )
    
    respuesta = st.text_area("📝 Comentarios o Consultas", height=100)
    
    # Espacio vacío
    st.write("")
    
    # Botón de envío que ocupa todo el ancho
    submitted = st.form_submit_button("ENVIAR REGISTRO 🚀", use_container_width=True)

    # --- 5. LÓGICA DE ENVÍO ---
    if submitted:
        if not nombre or not correo:
            st.warning("⚠️ Por favor, completa los campos obligatorios (Nombre y Correo).")
        else:
            # Empaquetamos los datos
            datos = {
                "nombre": nombre,
                "correo": correo,
                "curso": curso,
                "respuesta": respuesta
            }
            
            # Mostramos un spinner mientras carga
            with st.spinner("Conectando con el servidor..."):
                try:
                    # Enviamos a Google Sheets
                    r = requests.post(URL_APPS_SCRIPT, json=datos)
                    
                    if r.status_code == 200:
                        # --- EL CAMBIO: TOAST EN LUGAR DE GLOBOS ---
                        st.toast("¡Registro guardado correctamente!", icon="✅")
                        
                        # Mensaje fijo de confirmación
                        st.success(f"✅ ¡Listo! Te has registrado en **{curso}** exitosamente.")
                    else:
                        st.error("❌ Error interno del servidor.")
                except Exception as e:
                    st.error(f"📡 Error de conexión: {e}")

# Pie de página simple
st.markdown("---")
st.caption("© 2026 - Sistema de Registro Interno")
