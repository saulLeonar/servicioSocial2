import streamlit as st
#import plotly.graph_objects as go

incomes= ["Salary", "Blog", "Other Incomes"]
expenses=["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency="USD"
page_title = "Incomes and Expense Tracker"
page_icon=":money_with_wings"

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title+""+page_icon)
