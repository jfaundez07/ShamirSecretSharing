import unittest
from main import interpolacion_lagrange, generar_polinomio, obtener_partes

class TestInterpolacionLagrange(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para las pruebas
        self.secreto_correcto = 10  # Suponiendo que el secreto original es 1
        self.umbral = 4
        self.polinomio = generar_polinomio(self.secreto_correcto, self.umbral)
        self.partes = obtener_partes([11, 15, 21, 45, 13], self.polinomio)

    def test_recuperacion_correcta(self):
        # Prueba con el número correcto de partes
        secreto = interpolacion_lagrange(self.partes)
        self.assertEqual(secreto, self.secreto_correcto)

    def test_fuerza_bruta_con_menos_partes(self):
        # Prueba con menos partes de las necesarias
        partes_incompletas = self.partes[:3]  # Solo dos partes
        secreto = interpolacion_lagrange(partes_incompletas)
        # Verificamos que el secreto recuperado no sea el correcto
        self.assertNotEqual(secreto, self.secreto_correcto)

    def test_fuerza_bruta_con_partes_incorrectas(self):
        # Prueba con partes incorrectas
        partes_incorrectas = [(1, 3), (2, 5), (3, 8), (4, 10)]  # Cambiamos algunos valores
        secreto = interpolacion_lagrange(partes_incorrectas)
        self.assertNotEqual(secreto, self.secreto_correcto)

if __name__ == '__main__':
    unittest.main()