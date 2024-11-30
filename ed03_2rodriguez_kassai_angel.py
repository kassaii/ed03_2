"""
Calculadora científica con operaciones matemáticas
"""
import math
import logging
import sys

# Configuración del logging para escribir tanto en archivo como en consola
# Crear un formateador que usaremos para ambos handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Configurar el logger
logger = logging.getLogger('CalculadoraCientifica')
logger.setLevel(logging.INFO)

# Handler para archivo
file_handler = logging.FileHandler('calculadora.log')
file_handler.setFormatter(formatter)

# Handler para consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Añadir ambos handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

class CalculadoraCientifica:
    """
    Calculadora
    """
    def __init__(self):
        logger.info("Iniciando calculadora científica")

    def validar_numeros(self, *args):
        """Valida que los argumentos sean números"""
        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError(f"Se esperaba un número, se recibió {type(num)}")

    # Operaciones básicas
    def sumar(self, a, b):
        """Suma dos números"""
        self.validar_numeros(a, b)
        logger.info("Sumando %d + %d", a, b)
        return a + b

    def restar(self, a, b):
        """Resta dos números"""
        self.validar_numeros(a, b)
        logger.info("Restando %d - %d", a, b)
        return a - b

    def multiplicar(self, a, b):
        """Multiplica dos números"""
        self.validar_numeros(a, b)
        logger.info("Multiplicando %d * %d", a, b)
        return a * b

    def dividir(self, a, b):
        """Divide dos números"""
        self.validar_numeros(a, b)
        if b == 0:
            logger.error("Intento de división por cero")
            raise ValueError("No se puede dividir por cero")
        logger.info("Dividiendo %d / %d", a, b)
        return a / b

    # Operaciones avanzadas
    def potencia(self, base, exponente):
        """Calcula la potencia de un número"""
        self.validar_numeros(base, exponente)
        logger.info("Calculando %d ^ %d", base, exponente)
        return math.pow(base, exponente)

    def raiz_cuadrada(self, numero):
        """Calcula la raíz cuadrada de un número"""
        self.validar_numeros(numero)
        if numero < 0:
            logger.error("Intento de calcular raíz cuadrada de número negativo: %s", numero)
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        logger.info("Calculando raíz cuadrada de %d", numero)
        return math.sqrt(numero)

    def logaritmo_natural(self, numero):
        """Calcula el logaritmo natural de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo de número no positivo: %s", numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo natural de %d", numero)
        return math.log(numero)

    def logaritmo_base_10(self, numero):
        """Calcula el logaritmo en base 10 de un número"""
        self.validar_numeros(numero)
        if numero <= 0:
            logger.error("Intento de calcular logaritmo base 10 de número no positivo: %s", numero)
            raise ValueError("No se puede calcular el logaritmo de un número menor o igual a cero")
        logger.info("Calculando logaritmo base 10 de %d", numero)
        return math.log10(numero)

    def seno(self, angulo):
        """Calcula el seno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando seno de %f radianes", angulo)
        return math.sin(angulo)

    def coseno(self, angulo):
        """Calcula el coseno de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando coseno de %f radianes", angulo)
        return math.cos(angulo)

    def tangente(self, angulo):
        """Calcula la tangente de un ángulo en radianes"""
        self.validar_numeros(angulo)
        logger.info("Calculando tangente de %f radianes", angulo)
        return math.tan(angulo)

def main():
    """Función principal que interactúa con el usuario y realiza operaciones matemáticas."""
    # Crear instancia de la calculadora
    calc = CalculadoraCientifica()

    try:
        # Operaciones básicas
        print("\n=== Operaciones Básicas ===")
        a = float(input("Introduce el primer número para la suma: "))
        b = float(input("Introduce el segundo número para la suma: "))
        print(f"Suma de {a} + {b} = {calc.sumar(a, b)}")

        a = float(input("Introduce el primer número para la resta: "))
        b = float(input("Introduce el segundo número para la resta: "))
        print(f"Resta de {a} - {b} = {calc.restar(a, b)}")

        a = float(input("Introduce el primer número para la multiplicación: "))
        b = float(input("Introduce el segundo número para la multiplicación: "))
        print(f"Multiplicación de {a} * {b} = {calc.multiplicar(a, b)}")

        a = float(input("Introduce el primer número para la división: "))
        b = float(input("Introduce el segundo número para la división: "))
        print(f"División de {a} / {b} = {calc.dividir(a, b)}")

        # Operaciones avanzadas
        print("\n=== Operaciones Avanzadas ===")
        base = float(input("Introduce la base para la potencia: "))
        exponente = float(input("Introduce el exponente para la potencia: "))
        print(f"Potencia de {base} ^ {exponente} = {calc.potencia(base, exponente)}")

        numero = float(input("Introduce el número para la raíz cuadrada: "))
        print(f"Raíz cuadrada de {numero} = {calc.raiz_cuadrada(numero)}")

        numero = float(input("Introduce el número para el logaritmo natural: "))
        print(f"Logaritmo natural de {numero} = {calc.logaritmo_natural(numero)}")

        numero = float(input("Introduce el número para el logaritmo base 10: "))
        print(f"Logaritmo base 10 de {numero} = {calc.logaritmo_base_10(numero)}")

        # Funciones trigonométricas
        print("\n=== Funciones Trigonométricas ===")
        angulo = float(input("Introduce el ángulo en radianes para calcular el seno: "))
        print(f"Seno de {angulo} radianes = {calc.seno(angulo)}")

        angulo = float(input("Introduce el ángulo en radianes para calcular el coseno: "))
        print(f"Coseno de {angulo} radianes = {calc.coseno(angulo)}")

        angulo = float(input("Introduce el ángulo en radianes para calcular la tangente: "))
        print(f"Tangente de {angulo} radianes = {calc.tangente(angulo)}")

    except ValueError as e:
        logger.error("Error de valor: %s", str(e))
        print(f"Error de valor: {e}")
    except TypeError as e:
        logger.error("Error de tipo: %s", str(e))
        print(f"Error de tipo: {e}")
    except KeyError as e:
        logger.error("Error de clave: %s", str(e))
        print(f"Error de clave: {e}")
    except IndexError as e:
        logger.error("Error de índice: %s", str(e))
        print(f"Error de índice: {e}")

if __name__ == "__main__":
    main()
