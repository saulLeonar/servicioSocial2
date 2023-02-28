import calendar
from datetime import datetime 

import streamlit as st
#import plotly.graph_objects as go


#incomes= ["Salary", "Blog", "Other Incomes"]
#expenses=["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency="USD"
page_title = "Socio formadores"
page_icon=":office_worker:"
layout= "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)

years = [datetime.today().year, datetime.today().year+1]
months= list(calendar.month_name[1:])

st.header(f"Data Entry in {currency}")
with st.form("entry_form", clear_on_submit=True):
  col1,col2=st.columns(2)
  col1.selectbox("Select Month:",months, key="month")
  col2.selectbox("Select year:", years,key="year")



