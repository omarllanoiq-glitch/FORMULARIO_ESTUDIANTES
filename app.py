import streamlit as st
import pandas as pd
from datetime import date
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Portal de Gestión SENATI",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ESTILOS CSS PERSONALIZADOS (Para que se vea "Bonita" y con colores SENATI) ---
st.markdown("""
    <style>
    /* Color de fondo principal y fuentes */
    .main {
        background-color: #f8f9fa;
    }
    h1, h2, h3 {
        color: #2d3748;
    }
    /* Estilo para los botones (Naranja SENATI) */
    .stButton>button {
        background-color: #ea580c;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #c2410c;
        color: white;
        border: 1px solid #ea580c;
    }
    /* Estilo del Sidebar */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }
    /* Tarjetas personalizadas */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-top: 4px solid #ea580c;
        margin-bottom: 20px;
        color: #4b5563;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIONES DE LOS FORMULARIOS ---

def mostrar_home():
    # Header estilo Banner
    st.markdown("""
    <div style="background: linear-gradient(90deg, #ea580c 0%, #9a3412 100%); padding: 3rem; border-radius: 10px; color: white; margin-bottom: 2rem;">
        <h1 style="color: white; margin:0;">Portal de Gestión SENATI</h1>
        <p style="font-size: 1.2rem; margin-top: 10px;">Sistema integrado para empresas, estudiantes y convenios institucionales</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("### Seleccione un servicio:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>📄 Carta de Presentación</h3>
            <p>Solicita tu carta para postular a empresas.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ir a Cartas", key="btn_carta"):
            st.session_state.page = "Carta de Presentación"
            st.rerun()

        st.markdown("""
        <div class="card">
            <h3>🏢 Registro de Empresa</h3>
            <p>Registra tu empresa en nuestra red.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ir a Empresas", key="btn_empresa"):
            st.session_state.page = "Registro de Empresa"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🤝 Convenio Empresarial</h3>
            <p>Establece alianzas estratégicas.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ir a Convenios", key="btn_convenio"):
            st.session_state.page = "Solicitud de Convenio"
            st.rerun()

        st.markdown("""
        <div class="card">
            <h3>💼 Ofertas de Trabajo</h3>
            <p>Publica vacantes para egresados.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Ir a Ofertas", key="btn_oferta"):
            st.session_state.page = "Publicar Oferta"
            st.rerun()

def form_carta_presentacion():
    st.title("📄 Solicitud de Carta de Presentación")
    st.info("Complete sus datos para generar la carta oficial.")
    
    with st.form("form_carta"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre Completo")
            carrera = st.selectbox("Carrera Técnica", ["Electrotecnia Industrial", "Mecánica de Mantenimiento", "Electrónica Industrial", "Mecatrónica Industrial", "Administración Industrial"])
            telefono = st.text_input("Teléfono")
        with col2:
            dni = st.text_input("DNI")
            email = st.text_input("Email Institucional")
            empresa = st.text_input("Empresa de Destino (Opcional)")
        
        cv = st.file_uploader("Subir CV (PDF)", type=["pdf"])
        
        submitted = st.form_submit_button("Enviar Solicitud")
        if submitted:
            if nombre and dni and carrera:
                st.success("¡Solicitud enviada correctamente!")
                st.balloons()
                # Aquí iría el código para guardar en Google Sheets
            else:
                st.error("Por favor complete los campos obligatorios.")

def form_convenio():
    st.title("🤝 Solicitud de Convenio")
    
    with st.form("form_convenio"):
        col1, col2 = st.columns(2)
        with col1:
            empresa = st.text_input("Nombre de la Empresa")
            representante = st.text_input("Representante Legal")
            telefono = st.text_input("Teléfono de Contacto")
        with col2:
            ruc = st.text_input("RUC")
            email = st.text_input("Email Corporativo")
            tipo = st.selectbox("Tipo de Convenio", ["Prácticas Profesionales", "Formación Dual", "Capacitación In-House", "Bolsa de Trabajo"])
        
        desc = st.text_area("Descripción del interés")
        
        submitted = st.form_submit_button("Enviar Solicitud de Convenio")
        if submitted:
            st.success(f"Gracias {empresa}, nos pondremos en contacto pronto.")

def form_empresa():
    st.title("🏢 Registro de Nueva Empresa")
    
    with st.form("form_empresa"):
        col1, col2 = st.columns(2)
        with col1:
            razon_social = st.text_input("Razón Social")
            sector = st.selectbox("Sector", ["Manufactura", "Minería", "Construcción", "Servicios", "Tecnología"])
            ciudad = st.text_input("Ciudad")
            contacto = st.text_input("Persona de Contacto")
        with col2:
            ruc = st.text_input("RUC")
            direccion = st.text_input("Dirección Fiscal")
            email = st.text_input("Email")
            web = st.text_input("Sitio Web")
            
        submitted = st.form_submit_button("Registrar Empresa")
        if submitted:
            st.success("Empresa registrada en la base de datos.")

def form_oferta():
    st.title("💼 Publicar Oferta de Trabajo")
    
    with st.form("form_oferta"):
        titulo = st.text_input("Título del Puesto")
        col1, col2 = st.columns(2)
        with col1:
            empresa = st.text_input("Empresa")
            modalidad = st.selectbox("Modalidad", ["Presencial", "Remoto", "Híbrido"])
        with col2:
            area = st.selectbox("Área", ["Producción", "Mantenimiento", "Calidad", "Logística", "Administración"])
            tipo_contrato = st.selectbox("Contrato", ["Tiempo Completo", "Medio Tiempo", "Prácticas"])
            
        descripcion = st.text_area("Descripción del Puesto")
        requisitos = st.text_area("Requisitos")
        
        submitted = st.form_submit_button("Publicar Oferta")
        if submitted:
            st.success("La oferta ha sido publicada en la bolsa de trabajo.")

# --- NAVEGACIÓN LATERAL ---
if "page" not in st.session_state:
    st.session_state.page = "Inicio"

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/47/Senati_peru_logo.png", width=100) # Logo genérico SENATI
    st.title("Menú Principal")
    
    # Menú de navegación
    opcion = st.radio(
        "Ir a:",
        ["Inicio", "Carta de Presentación", "Solicitud de Convenio", "Registro de Empresa", "Publicar Oferta"],
        index=["Inicio", "Carta de Presentación", "Solicitud de Convenio", "Registro de Empresa", "Publicar Oferta"].index(st.session_state.page)
        if st.session_state.page in ["Inicio", "Carta de Presentación", "Solicitud de Convenio", "Registro de Empresa", "Publicar Oferta"] else 0
    )
    
    # Actualizar estado si cambia el radio button
    if opcion != st.session_state.page:
        st.session_state.page = opcion
        st.rerun()

    st.divider()
    st.info("📍 Puno, Perú")
    st.caption("© 2026 SENATI - UFP")

# --- CONTROLADOR DE PÁGINAS ---
if st.session_state.page == "Inicio":
    mostrar_home()
elif st.session_state.page == "Carta de Presentación":
    form_carta_presentacion()
elif st.session_state.page == "Solicitud de Convenio":
    form_convenio()
elif st.session_state.page == "Registro de Empresa":
    form_empresa()
elif st.session_state.page == "Publicar Oferta":
    form_oferta()
