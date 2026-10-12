
import csv
from pathlib import Path


RUTA_CSV = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "uso_ventilacion.csv"
)


def calcular_uso_ventilacion(velocidad_viento):
    if velocidad_viento <= 10:
        return round((10 - velocidad_viento) * 5, 2)

    return 0


def generar_csv_ventilacion(datos_meteorologicos):
    RUTA_CSV.parent.mkdir(parents=True, exist_ok=True)

    with open(RUTA_CSV, "w", newline="", encoding="utf-8") as archivo:
        campos = [
            "Día",
            "Velocidad del viento (km/h)",
            "Uso estimado de ventilación (kWh)"
        ]

        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()

        for dia in datos_meteorologicos:
            velocidad = dia["velocidad_viento"]

            if velocidad is None:
                continue

            uso = calcular_uso_ventilacion(velocidad)

            escritor.writerow({
                "Día": dia["dia"],
                "Velocidad del viento (km/h)": velocidad,
                "Uso estimado de ventilación (kWh)": uso
            })


if __name__ == "__main__":
    from src.api_meteorologica import obtener_datos_meteorologicos

    datos = obtener_datos_meteorologicos()
    generar_csv_ventilacion(datos)

    print(f"CSV generado correctamente: {RUTA_CSV}")
