import unittest

from src.calefaccion import calcular_consumo_calefaccion
from src.ventilacion import calcular_uso_ventilacion


class TestCalefaccion(unittest.TestCase):

    def test_temperatura_baja(self):
        self.assertEqual(calcular_consumo_calefaccion(10), 50)

    def test_temperatura_alta(self):
        self.assertEqual(calcular_consumo_calefaccion(20), 0)


class TestVentilacion(unittest.TestCase):

    def test_viento_bajo(self):
        self.assertEqual(calcular_uso_ventilacion(4), 30)

    def test_viento_alto(self):
        self.assertEqual(calcular_uso_ventilacion(12), 0)


if __name__ == "__main__":
    unittest.main()
