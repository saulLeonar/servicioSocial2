#import calendar
#from datetime import datetime 

import streamlit as st
#import plotly.graph_objects as go


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

##FRequisitos
#with st.expander("Requisitos para el alumno: "):
#  requirements= st.text_area("")
##Carreras
carreras=st.multiselct("Carreras:" ["Todas","Arquitecto", "Ingeniero Civil","Licenciado en Urbanismo""Licenciado en economía", "Licenciado en Derecho","Licenciado en Relaciones Internacionales", "Licenciado en Gobierno y transformación pública", "Licenciado en Arte digital","Licenciado en Comunicación","Licenciado en Diseño","Licenciado en Innovación Educativa","Licenciado en Letras Hispanicas","Licenciado en periodismo","Licenciado en Tecnología y producción musical","Ingeniero Biomedico", "Ingeniero en Electronica", "Ingeniero en innovacion y desarrollo","Ingeniero industrial y de sistemas","Ingeniero Mecanico","Ingniero Mecatronico"],["Todas"])
st.write(carreras)
 
