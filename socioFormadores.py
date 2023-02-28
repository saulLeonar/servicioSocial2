from datetime import time
import datetime
import streamlit as st


currency="Proyectos"
page_title = "Socio formadores"
page_icon=":office_worker:"
layout= "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)


st.header(f"Registro de {currency}")
with st.expander("Nombre del proyecto: "):
  name= st.text_area("",)
 
##Descripción del proyecto##
with st.expander("Descipción del proyecto: "):
  description= st.text_area("", placeholder="Ingresa aqui la descripcion del proyecto...")
 
##Cupo del grupo
st.number_input("Número de alumnos que se necesitan: ", min_value=0, format="%i", step= 1)

##Horas a acreditar##
st.number_input("Horas a acreditar: ", min_value=50, format="%i", step= 1)


##Carreras
carreras=st.multiselect("Seleccione carreras participantes: ", ["Todas","Arquitecto", "Ingeniero Civil","Licenciado en Urbanismo""Licenciado en economía", "Licenciado en Derecho","Licenciado en Relaciones Internacionales", "Licenciado en Gobierno y transformación pública", "Licenciado en Arte digital","Licenciado en Comunicación","Licenciado en Diseño","Licenciado en Innovación Educativa","Licenciado en Letras Hispanicas","Licenciado en periodismo","Licenciado en Tecnología y producción musical","Ingeniero Biomedico", "Ingeniero en Electronica", "Ingeniero en innovacion y desarrollo","Ingeniero industrial y de sistemas","Ingeniero Mecanico","Ingniero Mecatronico"])

## Requisitos
st.title("Requisitos")
requirements = st.text_area("Ingrese los requisitos, uno por línea")
requirements = requirements.split("\n")
requirements = list(filter(None, requirements))
if len(requirements) > 0:
  st.write("Requisitos:")
  for i, requirement in enumerate(requirements):
    st.write(f"{i+1}. {requirement}")

#Fechas
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)
start_date = st.date_input('Fecha de inicio', today)
end_date = st.date_input('Fecha de término', tomorrow)

# Horario
st.header("Horario de servicio")

# Default start and end time
start_time = time(8, 0)
end_time = time(18, 0)

# User-selectable time range
selected_time_range = st.slider("Select Time Range", value=(start_time, end_time), format="HH:mm")

# Display selected time range
st.write("Selected Time Range: {} - {}".format(selected_time_range[0].strftime("%H:%M"), selected_time_range[1].strftime("%H:%M")))

##Modalidad
modalidad= ["Presencial", "Remoto", "Hibrido"]
st.selectbox("Seleccione la modalidad",modalidad,key="Modalidad")

##Ubicación
st.header("Dirección")
# Calle y Número
calle_numero = st.text_input("Calle y Número")

# Colonia
colonia = st.text_input("Colonia")

# Ciudad, Estado y Código Postal
col1, col2, col3 = st.columns([2,1,2])
with col1:
    ciudad = st.text_input("Ciudad")
with col2:
    estado = st.selectbox("Estado", ["", "Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "Ciudad de México", "Durango", "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"])
with col3:
    codigo_postal = st.text_input("Código Postal")


##Actividades
st.title("Actividades")
act = st.text_area("Ingrese las actividades, una por línea")
act = act.split("\n")
act = list(filter(None, act))
if len(requirements) > 0:
  st.write("Actividades:")
  for i, act in enumerate(act):
    st.write(f"{i+1}. {act}")

##Entregables
st.title("Entregables")
entre = st.text_area("Ingrese los entregables, uno por línea")
entre = entre.split("\n")
entre = list(filter(None, entre))
if len(entre) > 0:
  st.write("Entregables:")
  for i, entre in enumerate(entre):
    st.write(f"{i+1}. {entre}")
##Costo
st.number_input("Costo de participación: ", min_value=0, format="%i", step= 1)

## Motivo del costo
with st.expander("Motivo del costo: "):
  costo_mot= st.text_area("",)

## Nombre del responsable
with st.expander("Nombre del responsable: "):
  name_resp= st.text_area("",)
 
## Medio de contacto
with st.expander("Medio de contacto"):
  num_tel= st.text_area("",placeholder="Ingrese su número de teléfono")
  correo= st.text_area("",placeholder="Ingrese su correo electrónico")
 

