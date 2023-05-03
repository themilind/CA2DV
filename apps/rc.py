#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Importing Libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from app import app


# In[13]:

# Load the customer shopping data
df = pd.read_csv("cleaned_customer_shopping_data.csv")

#Defining the layout with graphs and dropdowns
app.layout = html.Div([
    html.H4('Analysis of customer shopping data'),
    dcc.Graph(id="graph"),
    html.P("Categories:"),
    dcc.Dropdown(id='categories',
        options=[{'label': col, 'value': col} for col in df.columns],
        value='category', clearable=False
    ),
])

# Define the callback function
@app.callback(
    Output("graph", "figure"), 
    Input("categories", "value"))
def generate_chart(category):
    
    
    
# Group the data by the selected category and calculate the sum of the revenue for each group
    df_grouped = df.groupby(category, as_index=False)['Revenue'].sum()
    
# Create the pie chart
    fig = px.pie(df_grouped, values='Revenue', names=category, hole=.3)
    
    return fig


# In[ ]:




