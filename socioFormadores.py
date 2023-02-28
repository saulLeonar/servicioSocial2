import calendar
from datetime import datetime 

import streamlit as st
#import plotly.graph_objects as go


#incomes= ["Salary", "Blog", "Other Incomes"]
#expenses=["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
#currency="USD"
page_title = "Socio formadores"
page_icon=":office_worker:"
layout= "centered"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)

years = [datetime.today().year, datetime.today().year+1]
months= list(calendar.month_name[1:])


#st.header(f"Data Entryin {currency}")



