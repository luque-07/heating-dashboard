
import requests


URL_API = "https://api.open-meteo.com/v1/forecast"


def obtener_datos_meteorologicos(
    latitud=40.4168,
    longitud=-3.7038,
    dias=7
):
    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "daily": [
            "temperature_2m_mean",
            "wind_speed_10m_mean"
        ],
        "wind_speed_unit": "kmh",
        "timezone": "Europe/Madrid",
        "forecast_days": dias
    }

    respuesta = requests.get(
        URL_API,
        params=parametros,
        timeout=15
    )

    respuesta.raise_for_status()

    datos = respuesta.json()
    datos_diarios = datos["daily"]

    fechas = datos_diarios["time"]
    temperaturas = datos_diarios["temperature_2m_mean"]
    velocidades = datos_diarios["wind_speed_10m_mean"]

    if not (len(fechas) == len(temperaturas) == len(velocidades)):
        raise ValueError("La API ha devuelto series de distinta longitud.")

    resultados = []

    for i in range(len(fechas)):
        resultado_dia = {
            "dia": fechas[i],
            "temperatura_media": temperaturas[i],
            "velocidad_viento": velocidades[i]
        }

        resultados.append(resultado_dia)

    return resultados


if __name__ == "__main__":
    datos = obtener_datos_meteorologicos()

    for dia in datos:
        print(dia)
