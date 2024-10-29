from pymodbus.client import ModbusSerialClient
import time
from conversion import convert_temperature, convert_humidity, convert_pressure
from PS103J2_table import *
from dash import Dash, dcc, html, Input, Output, State



# Configuración del cliente Modbus RTU
client = ModbusSerialClient(
    port='COM25',       # Cambia 'COM25' al puerto que estés usando (por ejemplo, '/dev/ttyUSB0' en Linux)
    baudrate=9600,
    timeout=3,
    stopbits=1,
    bytesize=8,
    parity='N'
)

# Intenta conectar
if client.connect():
    print("Conectado al dispositivo Modbus")

    # Escribir 1 en el coil de la dirección 0 al iniciar
    coil_address = 0
    write_result = client.write_coil(coil_address, True, slave=3)
    if write_result.isError():
        print("Error al escribir en el coil:", write_result)
    else:
        print(f"Escrito 1 en el coil de la dirección {coil_address}")

    # Lee constantemente los registros y los asigna a cada parámetro en tiempo real
    try:
        while True:
            result = client.read_input_registers(address=2, count=6, slave=3)
            if result.isError():
                print("Error al leer los registros de entrada:", result)
            else:
                # Asignamos cada registro a su variable correspondiente
                temperatura_raw = result.registers[0]
                humedad_raw = result.registers[1]
                presion_parte_alta = result.registers[2]
                presion_parte_baja = result.registers[3]
                compensacion_alta = result.registers[4]
                compensacion_baja = result.registers[5]

                # Conversión de los valores
                temperatura = convert_temperature(temperatura_raw)
                humedad = convert_humidity(humedad_raw)
                presion = convert_pressure(presion_parte_alta, presion_parte_baja)

                # Imprimimos los valores con nombres específicos
                print(f"Temperatura: {temperatura:.2f} °C")
                print(f"Humedad: {humedad:.2f} %")
                print(f"Presión: {presion:.2f} hPa")
                print(f"Compensación (alta): {compensacion_alta}")
                print(f"Compensación (baja): {compensacion_baja}")

                # Reescribimos el coil en la dirección 0
                write_result = client.write_coil(coil_address, True, slave=3)
                if write_result.isError():
                    print("Error al escribir en el coil:", write_result)
                else:
                    print(f"Escrito 1 en el coil de la dirección {coil_address}")

            time.sleep(5)  # Espera 5 segundos antes de la siguiente lectura
    except KeyboardInterrupt:
        print("\nLectura en tiempo real detenida por el usuario.")

    # Cierra la conexión
    client.close()
else:
    print("No se pudo conectar al dispositivo Modbus")
