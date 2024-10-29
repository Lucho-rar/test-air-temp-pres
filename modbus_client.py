import logging
from pymodbus.client import ModbusSerialClient

# Configuración del cliente Modbus RTU
client = ModbusSerialClient(
    port='COM25',  # Cambia 'COM25' al puerto que estés usando
    baudrate=9600,
    timeout=10,
    stopbits=1,
    bytesize=8,
    parity='N'
)

def connect():
    """Conectar al cliente Modbus."""
    if not client.connect():
        raise ConnectionError("No se pudo conectar al cliente Modbus.")

def write_initial_coil():
    """Escribir en el coil inicial para activar el dispositivo."""
    connect()
    # Escribir 1 en el coil 0
    result = client.write_coil(address=0, value=True, slave=3)
    if result.isError():
        raise ValueError("Error al escribir en el coil.")

def read_data():
    """Leer datos del registro Modbus."""
    write_initial_coil()  # Asegúrate de activar el dispositivo antes de leer
    result = client.read_input_registers(address=2, count=6, slave=3)
    if result.isError():
        raise ValueError("Error al leer los registros Modbus.")
    
    # Agregar logging para verificar los valores leídos
    logging.info(f"Valores leídos: {result.registers}")
    return result.registers