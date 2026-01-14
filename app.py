import streamlit as st

st.set_page_config(page_title="Formulario SENATI", page_icon="⚙️")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #ea580c; 
        color: white; 
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #c2410c;
        color: white;
    }
    h1, h2, h3 { color: #1e3a8a; }
    </style>
""", unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/commons/4/47/Senati_peru_logo.png", width=80)
st.title("Registro de Estudiantes")

with st.form("mi_formulario"):
    id_estudiante = st.text_input("ID del Estudiante", placeholder="Ej: 001234")
    nombre = st.text_input("Nombre Completo")
    carrera = st.selectbox("Carrera", ["Ingeniería de Software", "Mecatrónica", "Electrotecnia", "Administración Ind."])
    
    enviado = st.form_submit_button("Registrar Alumno")

    if enviado:
        st.success(f"✅ Alumno {nombre} registrado.")
