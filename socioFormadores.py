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
 
##Descripccion del proyecto##
with st.expander("Descipción del proyecto: "):
  description= st.text_area("", placeholder="Ingresa aqui la descripcion del proyecto...")
 
##cupo del grupo
st.number_input("Numero de alumnos que se necsita: ", min_value=0, format="%i", step= 1)

##Horas acreditar##
st.number_input("Horas acreditar: ", min_value=50, format="%i", step= 1)

##FRequisitos
#with st.expander("Requisitos para el alumno: "):
#  requirements= st.text_area("")
##Carreras
carreras=["Todas","Arquitecto", "Ingeniero Civil","Licenciado en Urbanismo"]
with st.form("entry_form", clear_on_submit=True):
  col1, col2=st.columns(2)
  col1=selectbox("Seleccione las carreras que pueden participar:", carreras , key="carreras")
 
