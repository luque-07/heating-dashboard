# Heating Dashboard

Proyecto en Python que obtiene datos meteorológicos de Open-Meteo, calcula el consumo estimado de calefacción y el uso estimado de ventilación, genera archivos CSV y crea dashboards HTML interactivos con ECharts.

## Funcionalidades

- Obtención de previsiones meteorológicas para los próximos 7 días.
- Cálculo del consumo estimado de calefacción.
- Cálculo del uso estimado de ventilación.
- Exportación de datos a archivos CSV.
- Generación automática de dos dashboards HTML con ECharts.
- Tests automáticos para comprobar los cálculos.

## Tecnologías

- Python
- Open-Meteo API
- CSV
- ECharts
- unittest

## Requisitos

- Python 3.13 o compatible.
- Conexión a Internet para consultar la API meteorológica.

## Instalación

Clona el repositorio:

    git clone https://github.com/luque-07/heating-dashboard.git
    cd heating-dashboard

Crea y activa un entorno virtual en Windows:

    python -m venv .venv
    .venv\Scripts\Activate.ps1

Instala las dependencias:

    pip install -r requirements.txt

## Ejecución

### Generar los datos de calefacción

    python -m src.calefaccion

### Generar los datos de ventilación

    python -m src.ventilacion

### Generar los dashboards HTML

    python -m src.generar_dashboard

Los archivos generados se guardan en estas rutas:

- `data/consumo_calefaccion.csv`
- `data/uso_ventilacion.csv`
- `output/dashboard_calefaccion.html`
- `output/dashboard_ventilacion.html`

Abre los archivos HTML en un navegador para consultar los gráficos interactivos.

## Cálculos

### Calefacción

Si la temperatura media diaria es igual o inferior a 15 °C:

`Consumo = (15 - temperatura) × 10`

Si supera los 15 °C, el consumo estimado es de 0 kWh.

### Ventilación

Si la velocidad media diaria del viento es igual o inferior a 10 km/h:

`Uso = (10 - velocidad del viento) × 5`

Si supera los 10 km/h, el uso estimado es de 0 kWh.

## Tests

Ejecuta las pruebas automáticas:

    python -m unittest discover -s tests -v

Las pruebas comprueban los cálculos de calefacción y ventilación para distintos valores de entrada.

## Estructura del proyecto

    heating-dashboard/
    ├── data/
    │   ├── consumo_calefaccion.csv
    │   └── uso_ventilacion.csv
    ├── output/
    │   ├── dashboard_calefaccion.html
    │   └── dashboard_ventilacion.html
    ├── src/
    │   ├── api_meteorologica.py
    │   ├── calefaccion.py
    │   ├── ventilacion.py
    │   └── generar_dashboard.py
    ├── tests/
    │   └── test_calculos.py
    ├── .gitignore
    ├── README.md
    └── requirements.txt

## Fuente de datos

Los datos meteorológicos se obtienen de [Open-Meteo](https://open-meteo.com/).

Los dashboards utilizan [Apache ECharts](https://echarts.apache.org/) para representar los datos mediante gráficos interactivos.