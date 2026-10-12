
import csv
from pathlib import Path


RUTA_CSV = Path(__file__).resolve().parent.parent / "data" / "consumo_calefaccion.csv"


def calcular_consumo_calefaccion(temperatura):
    if temperatura <= 15:
        return round((15 - temperatura) * 10, 2)

    return 0


def generar_csv_calefaccion(datos_meteorologicos):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open(RUTA_CSV, "w", newline="", encoding="utf-8") as archivo:
        campos = [
            "Día",
            "Temperatura media (°C)",
            "Consumo de calefacción (kWh)"
        ]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for dia in datos_meteorologicos:
            temperatura = dia["temperatura_media"]

            if temperatura is None:
                continue

            consumo = calcular_consumo_calefaccion(temperatura)

            escritor.writerow({
                "Día": dia["dia"],
                "Temperatura media (°C)": temperatura,
                "Consumo de calefacción (kWh)": consumo
            })

if __name__ == "__main__":
    from src.api_meteorologica import obtener_datos_meteorologicos

    datos = obtener_datos_meteorologicos()
    generar_csv_calefaccion(datos)
    
    print(f"CSV generado correctamente: {RUTA_CSV}")
