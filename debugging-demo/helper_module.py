"""
Módulo auxiliar usado por el demo de depuración.
Contiene una función que realiza varios pasos para que sea fácil poner breakpoints y hacer 'step into'.
"""

import math


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
