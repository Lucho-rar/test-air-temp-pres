# conversion.py
from PS103J2_table import *  # Importa la tabla de termistores

def convert_temperature(value):
    """Convierte el valor del registro de temperatura a grados Celsius usando la tabla de termistores."""
    if value != 4444:  # Si el valor no es el indicador de error
        RNTC = (value * 20000) / (4096 - value)  # Cálculo de resistencia
        index = closest(PS103J2_array, RNTC)  # Obtener el índice del valor más cercano
        return PS103J2_temp_array[index]  # Retornar la temperatura correspondiente
    return 0  # Retorna 0 en caso de error


def convert_humidity(value):
    """Convierte el valor de humedad a porcentaje."""
    if value != 4444:  # Si el valor no es el indicador de error
        return (value / 65536) * 100  # Conversión a porcentaje
    return 0  # Retorna 0 en caso de error

def convert_pressure(high, low):
    """Convierte los registros de presión a hPa (ejemplo)."""
    if high != 4444 and low != 4444:  # Si los valores no son indicadores de error
        pressure = (high << 16) | low  # Combinando los registros de alta y baja
        return pressure / 100.0  # Conversión a hPa
    return 0  # Retorna 0 en caso de error
