from dash import Dash, dcc, html, Input, Output

from pandas import read_csv

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Scrim file name:"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])

@app.callback(
    Output(component_id='',component_property='figure'),
    Input(component_id='my-input',component_property='value')
)
def update_figure(input_file):
    df = read_csv(input_file)

    