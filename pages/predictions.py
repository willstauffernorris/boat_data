# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
pipeline = load('assets/pipeline.joblib')


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### Day of the Year'), 
        dcc.Slider(
            id='Day_of_year', 
            min=1, 
            max=365, 
            step=5, 
            value=150, 
            marks={n: str(n) for n in range(1,365,50)}, 
            className='mb-5', 
        ), 
        
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Expected Revenue', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)


import pandas as pd

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Day_of_year', 'value')],
)
def predict(Day_of_year):
    df = pd.DataFrame(
        columns=['Day_of_year'], 
        data=[[Day_of_year]]
    )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred:.0f} dollars'

layout = dbc.Row([column1, column2])