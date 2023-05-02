#!/usr/bin/env python
# coding: utf-8

# In[13]:


from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# In[ ]:


# Connect to main app.py file
from app import app
from app import server


# Connect to your app pages
from apps import tc, sm, rc



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Table Chart ', href='/apps/tc'),
        dcc.Link('Revenue Across Shopping Malls ', href='/apps/sm'),
        dcc.Link('Revenue Category ', href='/apps/rc'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/tc':
        return tc.layout
    if pathname == '/apps/sm':
        return sm.layout
    if pathname == '/apps/rc':
        return rc.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:




