# app.py
from dash import Dash, dcc, html
import webbrowser
import logging  # Importa el módulo logging
from callbacks import register_callbacks

# Configuración del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inicialización de la aplicación Dash
app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f4f4f4', 'padding': '20px'}, children=[
    html.H1("Monitoreo Humedad-Temp-Presion", style={'textAlign': 'center', 'color': '#333'}),
    
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0),
    
    html.Button("Iniciar/Detener Log", id='boton-log', n_clicks=0, style={'fontSize': 18, 'padding': '10px'}),
    dcc.Store(id='estado-log', data=False),  # Almacena el estado del logging
    
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap'}, children=[
        html.Div(id='live-update-temperatura', style={'fontSize': 24, 'backgroundColor': '#ffcccb', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'margin': '10px'}),
        html.Div(id='live-update-humedad', style={'fontSize': 24, 'backgroundColor': '#add8e6', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'margin': '10px'}),
        html.Div(id='live-update-presion', style={'fontSize': 24, 'backgroundColor': '#90ee90', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'margin': '10px'}),
    ]),
    
    html.Div(style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap'}, children=[
        html.Div(id='live-update-comp-alta', style={'fontSize': 24, 'backgroundColor': '#ffeb3b', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'margin': '10px'}),
        html.Div(id='live-update-comp-baja', style={'fontSize': 24, 'backgroundColor': '#ffa07a', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'margin': '10px'}),
    ]),
    
    html.Div(id='live-update-ultima', style={'fontSize': 20, 'marginTop': 20, 'textAlign': 'center', 'color': '#555'})
])

# Registro de callbacks
register_callbacks(app)

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050')
    app.run_server(debug=True)