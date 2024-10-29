# callbacks.py
from datetime import datetime
from dash import Input, Output, State
from modbus_client import read_data, write_initial_coil  # Asegúrate de tener esta función
from conversion import convert_temperature, convert_humidity, convert_pressure
import logging
from PS103J2_table import *

# Inicializar las variables para los últimos valores válidos
ultimos_valores = {
    'temperatura': 'Temperatura: N/A',
    'humedad': 'Humedad: N/A',
    'presion': 'Presión: N/A',
    'compensacion_alta': 'Compensación (alta): N/A',
    'compensacion_baja': 'Compensación (baja): N/A',
    'ultima_actualizacion': 'Última actualización: N/A'
}

def guardar_datos_en_txt(datos):
    ruta_archivo = 'registro_datos.txt'
    with open(ruta_archivo, 'a') as archivo:
        archivo.write(datos + '\n')

def register_callbacks(app):
    @app.callback(
        Output('estado-log', 'data'),
        Input('boton-log', 'n_clicks'),
        State('estado-log', 'data')
    )
    def toggle_logging(n_clicks, estado_actual):
        if n_clicks > 0:
            return not estado_actual
        return estado_actual

    @app.callback(
        Output('live-update-temperatura', 'children'),
        Output('live-update-humedad', 'children'),
        Output('live-update-presion', 'children'),
        Output('live-update-comp-alta', 'children'),
        Output('live-update-comp-baja', 'children'),
        Output('live-update-ultima', 'children'),
        Input('interval-component', 'n_intervals'),
        State('estado-log', 'data')
    )
    def update_data(n, estado_log):
        global ultimos_valores  # Asegúrate de que puedes acceder a la variable global

        try:
            write_initial_coil()  # Asegúrate de activar el dispositivo antes de leer
            registers = read_data()
            temperatura = convert_temperature(registers[0])
            humedad = convert_humidity(registers[1])
            presion = convert_pressure(registers[2], registers[3])
            compensacion_alta = registers[4]
            compensacion_baja = registers[5]
            ultima_actualizacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Guardar datos si el logging está activo
            if estado_log:
                datos_a_guardar = f"{ultima_actualizacion}, {temperatura:.2f}, {humedad:.2f}, {presion:.2f}, {compensacion_alta}, {compensacion_baja}"
                guardar_datos_en_txt(datos_a_guardar)

            # Actualizar los valores
            ultimos_valores['temperatura'] = f"Temperatura: {temperatura:.2f} °C"
            ultimos_valores['humedad'] = f"Humedad: {humedad:.2f} %"
            ultimos_valores['presion'] = f"Presión: {presion:.2f} hPa"
            ultimos_valores['compensacion_alta'] = f"Compensación (alta): {compensacion_alta}"
            ultimos_valores['compensacion_baja'] = f"Compensación (baja): {compensacion_baja}"
            ultimos_valores['ultima_actualizacion'] = f"Última actualización: {ultima_actualizacion}"

        except (ConnectionError, ValueError, PermissionError) as e:
            logging.error(f"Error al leer datos: {e}")
            # Si hay un error, mantener los valores anteriores
            pass

        # Retornar los valores actuales, que pueden ser nuevos o anteriores
        return (
            ultimos_valores['temperatura'],
            ultimos_valores['humedad'],
            ultimos_valores['presion'],
            ultimos_valores['compensacion_alta'],
            ultimos_valores['compensacion_baja'],
            ultimos_valores['ultima_actualizacion']
        )