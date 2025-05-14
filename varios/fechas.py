from datetime import datetime

def dias_entre_fechas(f1, f2):
    formato = "%d/%m/%Y"
    fecha1 = datetime.strptime(f1, formato)
    fecha2 = datetime.strptime(f2, formato)
    diferencia = abs((fecha2 - fecha1).days)
    return diferencia

def main():
    f1 = "28/04/2023"
    f2 = "02/05/2024"
    f3 = "15/08/2023"
    dias1 = dias_entre_fechas(f1, f2)
    dias2 = dias_entre_fechas(f1, f3)
    print(f"Días entre {f1} y {f2}: {dias1} ")
    print(f"Días entre {f1} y {f3}: {dias2} ")

if __name__ == "__main__":
    main()