import streamlit as st
st.title('Mi Primera Aplicación en Streamlit')
st.title("Formulario Interactivo con Widgets")
st.title('Jose Hidalgo Torres')

#Para colocar widgets de ejemplo en el lateral
st.sidebar.title("Menú Lateral")

# 1. Input Box (Donde vamos a ingresar la edad, ingresando un valor numerico o haciendo uso de los signos + o - para ir aumentando o disminuyendo el # ingresado)
edad = st.sidebar.number_input("Ingrese su edad:", min_value=0, max_value=100, step=1)

# 2. Text Input (Donde ingresaremos nuestros nombres y apellidos)
nombre = st.sidebar.text_input("Ingrese su nombre completo:")

# 3. Slider (Donde vamos a ingresar el mes por medio de un selector numerico que cambia un paso a la vez)
mes = st.sidebar.slider("Seleccione un mes:", min_value=1, max_value=12)

# 4. Radio Buttons (El selector del genero, se puede seleccionar uno a la vez)
genero = st.sidebar.radio("Seleccione su género:", ["Masculino", "Femenino", "Otro"])

# 5. Selectbox (Se selecciona un pais de una lista desplegable pre rellenada y solo se limita a seleccionar los paises de la lista programada)
pais = st.sidebar.selectbox("Seleccione su país:", ["Ecuador", "Chile", "Colombia", "México", "Perú", "España"])

# La informacion del area principal:
st.header("Área Principal")

# Mostrar la información seleccionada
st.write("### Resumen de la Información")
st.write(f"**Nombre:** {nombre}")
st.write(f"**Edad:** {edad}")
st.write(f"**Mes Seleccionado:** {mes}")
st.write(f"**Género:** {genero}")
st.write(f"**País:** {pais}")

# 6. File Uploader (Simulacion de la carga de un archivo)
archivo = st.file_uploader("Cargue un archivo:", type=["jpg", "png", "pdf", "txt"])
if archivo is not None:
    st.write(f"Archivo cargado: {archivo.name}")

# 7. Date Input (Para seleccionar una fecha)
fecha = st.date_input("Seleccione una fecha:")
st.write(f"Fecha seleccionada: {fecha}")

# 8. Time Input (Para seleccionar una hora)
hora = st.time_input("Seleccione una hora:")
st.write(f"Hora seleccionada: {hora}")

# 9. Checkbox (Una pequeña caja donde se dara un click para hacer un check en "acepta_terminos")
acepta_terminos = st.checkbox("Acepto los términos y condiciones")

# 10. Button (Una vez ingresados los datos anteriores, enviar la informacion, considerando que se debe haber activado la casilla checkbox acepta_terminos)
if st.button("Enviar Información"):
    if acepta_terminos:
        st.info("Aceptaste los términos y condiciones.")
        st.success(f"¡Información enviada! \nNombre: {nombre} \nEdad: {edad} \nMes: {mes} \nGénero: {genero} \nPaís: {pais}")
    else:
        st.warning("Debes aceptar los términos para enviar la información.")