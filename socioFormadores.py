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

##Horas acreditar##
with st.form("entry_form", clear_on_submit=True):
  col1,col2=st.columns(2)
  col1.selectbox("Selecciona limite de horas a acreditar:", hora, key="hora")
  


