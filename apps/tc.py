#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from app import app

# Load data
df = pd.read_csv("cleaned_customer_shopping_data.csv")

# define layout
app.layout = html.Div([
    html.H1('Shopping Data Table'),
    dcc.Graph(id='data-table', figure={
        'data': [
            go.Table(
                header=dict(values=list(df.columns),
                            fill_color='paleturquoise',
                            align='left'),
                cells=dict(values=[df[col] for col in df.columns],
                           fill_color='lavender',
                           align='left')
            )
        ],
        'layout': go.Layout(
            title='Shopping Data Table'
        )
    })
])

@app.callback(
    Output('table_out', 'children'), 
    Input('table', 'active_cell'))
def update_graphs(active_cell):
    if active_cell:
        cell_data = df.iloc[active_cell['row']][active_cell['column_id']]
        return f"Data: \"{cell_data}\" from table cell: {active_cell}"
    return "Click the table"

# In[ ]:




