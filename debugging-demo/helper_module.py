"""
Módulo auxiliar usado por el demo de depuración.
Contiene una función que realiza varios pasos para que sea fácil poner breakpoints y hacer 'step into'.
"""

import math
import numpy as np
import pandas as pd

# Funcion que me diga el dia de la semana para una fecha dada   
def get_weekday(date_str):
    """Devuelve el día de la semana para una fecha dada.

    Args:
        date_str (str): Fecha en formato 'YYYY-MM-DD'.

    Returns:
        str: Día de la semana (por ejemplo, 'Monday').
    """
    date = pd.to_datetime(date_str)
    return date.strftime('%A')



def calculate_future_date(start_date, days_ahead):
    """Calcula una fecha futura sumando días a la fecha inicial.

    Args:
        start_date (str): Fecha inicial en formato 'YYYY-MM-DD'.
        days_ahead (int): Número de días a sumar.

    Returns:
        str: Fecha futura en formato 'YYYY-MM-DD'.
    """
    date = pd.to_datetime(start_date)
    future_date = date + pd.Timedelta(days=days_ahead)
    return future_date.strftime('%Y-%m-%d')
np.random

def compute_statistics(values):
    """Computa media, desviación estándar y máximo.

    Args:
        values (list[float]): lista de números

    Returns:
        dict: {'mean': ..., 'std': ..., 'max': ...}
    """
    if not values:
        raise ValueError("La lista 'values' no puede estar vacía")

    n = len(values)
    total = sum(values)
    mean = total / n

    # desviación estándar (poblacional)
    variance = sum((x - mean) ** 2 for x in values) / n
    std = math.sqrt(variance)

    maximum = max(values)

    # paso intermedio para depuración
    processed = [round(x, 3) for x in values]

    return {
        'mean': mean,
        'std': std,
        'max': maximum,
        'processed': processed,
        'count': n,
    }


def transform_and_sum(values, multiplier=1.0):
    """Transforma la lista multiplicando y sumando un offset calculado.

    Esta función llama a compute_statistics internamente para que puedas "step into".
    """
    if multiplier == 0:
        # ejemplo de rama a inspeccionar
        return 0

    offset = sum(values) * 0.01
    transformed = [(x * multiplier) + offset for x in values]

    stats = compute_statistics(transformed)

    return stats['mean'] * stats['count']
