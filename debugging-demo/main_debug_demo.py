"""
Demo principal para mostrar cómo depurar desde `main` a otro módulo.
Ejecuta varias llamadas que permiten usar `breakpoint()` o `python -m pdb` y seguir la ejecución.
"""
from helper_module import compute_statistics, transform_and_sum


def generate_sample_data(n=10):
    """Genera datos de ejemplo: una secuencia de números con algo de ruido."""
    import random
    random.seed(0)
    return [round(random.uniform(0, 100) + (i * 0.5), 4) for i in range(n)]


def main():
    data = generate_sample_data(12)
    print("Datos de entrada:", data)

    print("Llamando a transform_and_sum with multiplier=1.5")
    result = transform_and_sum(data, multiplier=1.5)
    print("Resultado transform_and_sum:", result)

    print("Ahora calculamos estadísticas directamente (entra en compute_statistics)")
    stats = compute_statistics(data)
    print("Estadísticas:")
    for k, v in stats.items():
        print(f"  {k}: {v}")


if __name__ == '__main__':
    main()
