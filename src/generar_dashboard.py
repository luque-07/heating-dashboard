
import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


def leer_csv(ruta):
    with open(ruta, "r", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def generar_html(datos, configuracion, ruta_salida):
    dias = [fila["Día"] for fila in datos]
    valores_principales = [
        float(fila[configuracion["campo_principal"]])
        for fila in datos
    ]
    valores_secundarios = [
        float(fila[configuracion["campo_secundario"]])
        for fila in datos
    ]

    datos_js = json.dumps(
        {
            "dias": dias,
            "principal": valores_principales,
            "secundario": valores_secundarios
        },
        ensure_ascii=False
    )

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{configuracion["titulo"]}</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5/dist/echarts.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f4f6f9;
            color: #222;
        }}
        h1 {{
            text-align: center;
        }}
        .grafica {{
            width: 100%;
            height: 350px;
            margin-bottom: 20px;
            background: white;
        }}
    </style>
</head>
<body>
    <h1>{configuracion["titulo"]}</h1>

    <div id="graficaPrincipal" class="grafica"></div>
    <div id="graficaSecundaria" class="grafica"></div>

    <script>
        const datos = {datos_js};

        const graficaPrincipal = echarts.init(
            document.getElementById("graficaPrincipal")
        );
        const graficaSecundaria = echarts.init(
            document.getElementById("graficaSecundaria")
        );

        graficaPrincipal.setOption({{
            title: {{ text: "{configuracion["titulo_principal"]}" }},
            tooltip: {{ trigger: "axis" }},
            grid: {{ left: 75, right: 30, bottom: 45 }},
            xAxis: {{
                type: "category",
                data: datos.dias,
                name: "Día"
            }},
            yAxis: {{
                type: "value",
                name: "{configuracion["eje_principal"]}"
            }},
            series: [{{
                name: "{configuracion["serie_principal"]}",
                type: "line",
                data: datos.principal,
                smooth: true
            }}]
        }});

        graficaSecundaria.setOption({{
            title: {{ text: "{configuracion["titulo_secundario"]}" }},
            tooltip: {{ trigger: "axis" }},
            grid: {{ left: 75, right: 30, bottom: 45 }},
            xAxis: {{
                type: "category",
                data: datos.dias,
                name: "Día"
            }},
            yAxis: {{
                type: "value",
                name: "{configuracion["eje_secundario"]}"
            }},
            series: [{{
                name: "{configuracion["serie_secundaria"]}",
                type: "bar",
                data: datos.secundario
            }}]
        }});

        window.addEventListener("resize", () => {{
            graficaPrincipal.resize();
            graficaSecundaria.resize();
        }});
    </script>
</body>
</html>
"""

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    ruta_salida.write_text(html, encoding="utf-8")
    print(f"Dashboard generado: {ruta_salida}")


def main():
    datos_calefaccion = leer_csv(
        DATA_DIR / "consumo_calefaccion.csv"
    )
    datos_ventilacion = leer_csv(
        DATA_DIR / "uso_ventilacion.csv"
    )

    generar_html(
        datos_calefaccion,
        {
            "titulo": "Dashboard de calefacción",
            "campo_principal": "Temperatura media (°C)",
            "campo_secundario": "Consumo de calefacción (kWh)",
            "titulo_principal": "Temperatura media diaria",
            "titulo_secundario": "Consumo estimado de calefacción",
            "eje_principal": "Temperatura (°C)",
            "eje_secundario": "Consumo (kWh)",
            "serie_principal": "Temperatura media",
            "serie_secundaria": "Consumo de calefacción"
        },
        OUTPUT_DIR / "dashboard_calefaccion.html"
    )

    generar_html(
        datos_ventilacion,
        {
            "titulo": "Dashboard de ventilación",
            "campo_principal": "Velocidad del viento (km/h)",
            "campo_secundario": "Uso estimado de ventilación (kWh)",
            "titulo_principal": "Velocidad media diaria del viento",
            "titulo_secundario": "Uso estimado de ventilación",
            "eje_principal": "Velocidad (km/h)",
            "eje_secundario": "Uso estimado (kWh)",
            "serie_principal": "Velocidad del viento",
            "serie_secundaria": "Uso de ventilación"
        },
        OUTPUT_DIR / "dashboard_ventilacion.html"
    )


if __name__ == "__main__":
    main()
