import streamlit as st
import requests

# --- CAMBIA ESTO POR TU URL DE APPS SCRIPT ---
URL_APPS_SCRIPT = "https://script.google.com/macros/s/AKfycbwfkvRYuit-2l79v3wgFJEmMuIRt3_SCbGvuG3c5Z90aUv7snPM2wlrJ4mHiJfEhu1YWw/exec"

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
