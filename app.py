import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Formulario SENATI", page_icon="⚙️")

# --- ESTILOS VISUALES (COLORES SENATI) ---
# Esto pinta el botón de naranja y ajusta los títulos
st.markdown("""
    <style>
    /* Botón naranja SENATI */
    .stButton>button {
        background-color: #ea580c; 
        color: white; 
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #c2410c; /* Un naranja un poco más oscuro al pasar el mouse */
        color: white;
    }
    /* Títulos en azul oscuro */
    h1, h2, h3 {
        color: #1e3a8a;
    }
    </style>
""", unsafe_allow_html=True)

# --- ENCABEZADO ---
st.image("https://upload.wikimedia.org/wikipedia/commons/4/47/Senati_peru_logo.png", width=80)
st.title("Registro de Estudiantes")
st.write("Ingresa los datos del alumno a continuación:")

# --- FORMULARIO ---
with st.form("mi_formulario"):
    # Campo 1: ID
    id_estudiante = st.text_input("ID del Estudiante (ID)", placeholder="Ej: 00123456")
    
    # Campo 2: Nombre
    nombre = st.text_input("Nombre Completo")
    
    # Campo 3: Carrera
    carrera = st.selectbox("Selecciona la Carrera", [
        "Ingeniería de Software",
        "Mecatrónica Industrial",
        "Electrotecnia",
        "Mecánica Automotriz",
        "Administración Industrial"
    ])
    
    # Botón de envío
    enviado = st.form_submit_button("Registrar Alumno")

    # --- LÓGICA AL PRESIONAR EL BOTÓN ---
    if enviado:
        if id_estudiante and nombre:
            st.success(f"✅ ¡Estudiante {nombre} ({carrera}) registrado correctamente!")
            # Aquí más adelante agregaremos el código para guardar en Excel/Google Sheets
        else:
            st.warning("⚠️ Por favor completa el ID y el Nombre.")
