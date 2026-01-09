import streamlit as st
import requests

# --- CAMBIA ESTO POR TU URL DE APPS SCRIPT ---
URL_APPS_SCRIPT = "AQUI_PEGAS_TU_URL_DE_APPS_SCRIPT_QUE_TERMINA_EN_EXEC"

st.title("📝 Formulario Estudiantes")

with st.form("mi_formulario"):
    nombre = st.text_input("Nombre completo")
    correo = st.text_input("Correo electrónico")
    respuesta = st.text_area("Comentario")
    
    submitted = st.form_submit_button("Enviar")

    if submitted:
        if not nombre:
            st.error("Falta el nombre")
        else:
            datos = {"nombre": nombre, "correo": correo, "respuesta": respuesta}
            try:
                r = requests.post(URL_APPS_SCRIPT, json=datos)
                if r.status_code == 200:
                    st.success("¡Enviado!")
                else:
                    st.error("Error al enviar")
            except:
                st.error("Error de conexión")
