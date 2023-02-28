#import calendar
#from datetime import datetime 

import streamlit as st
#import plotly.graph_objects as go


#incomes= ["Salary", "Blog", "Other Incomes"]
#expenses=["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency="Proyectos"
page_title = "Socio formadores"
page_icon=":office_worker:"
layout= "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)



hora=["0","1","2","3","4","5"]

st.header(f"Registro de {currency}")
##Descripccion del proyecto##
with st.expander("Descipción del proyecto: "):
  description= st.text_area("", placeholder="Ingresa aqui la descripcion del proyecto...")
 
##cupo del grupo
st.number_input("Numero de alumnos que se necsita: ", min_value=0, format="%i", step= 1)

##Horas acreditar##
st.number_input("Horas acreditar: ", min_value=50, format="%i", step= 1)

  


