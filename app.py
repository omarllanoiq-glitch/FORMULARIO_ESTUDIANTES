import streamlit as st
import requests

# --- TU URL DE APPS SCRIPT (Asegúrate de que sea la tuya) ---
URL_APPS_SCRIPT = "TU_URL_ORIGINAL_AQUI" 

st.title("📝 Formulario de Estudiantes")

with st.form("mi_formulario"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    
    # --- NUEVO: SELECTOR DE CURSO ---
    curso = st.selectbox(
        "Selecciona tu Curso/Carrera:",
        ["Mecánica Automotriz", "Ingeniería de Software", "Electricidad Industrial", "Administración", "Otro"]
    )
    
    respuesta = st.text_area("Comentario o Consulta")
    
    submitted = st.form_submit_button("Enviar Datos")

    if submitted:
        if not nombre:
            st.error("Por favor escribe tu nombre.")
        else:
            # Agregamos 'curso' al paquete de datos
            datos = {
                "nombre": nombre, 
                "correo": correo, 
                "curso": curso, 
                "respuesta": respuesta
            }
            
            try:
                r = requests.post(URL_APPS_SCRIPT, json=datos)
                if r.status_code == 200:
                    st.success(f"¡Registrado en el curso de {curso}!")
                else:
                    st.error("Error al enviar.")
            except:
                st.error("Error de conexión.")
