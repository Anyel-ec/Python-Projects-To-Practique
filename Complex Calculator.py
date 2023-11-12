class CalculadoraCompleja:
    def __init__(self, real, imaginaria):
        self.real = real
        self.imaginaria = imaginaria

    def __str__(self):
        return f"{self.real} + {self.imaginaria}i"

    def suma(self, otro):
        nueva_real = self.real + otro.real
        nueva_imaginaria = self.imaginaria + otro.imaginaria
        return CalculadoraCompleja(nueva_real, nueva_imaginaria)

    def resta(self, otro):
        nueva_real = self.real - otro.real
        nueva_imaginaria = self.imaginaria - otro.imaginaria
        return CalculadoraCompleja(nueva_real, nueva_imaginaria)

    def multiplicacion(self, otro):
        nueva_real = (self.real * otro.real) - (self.imaginaria * otro.imaginaria)
        nueva_imaginaria = (self.real * otro.imaginaria) + (self.imaginaria * otro.real)
        return CalculadoraCompleja(nueva_real, nueva_imaginaria)

    def division(self, otro):
        denominador = otro.real**2 + otro.imaginaria**2
        nueva_real = (self.real * otro.real + self.imaginaria * otro.imaginaria) / denominador
        nueva_imaginaria = (self.imaginaria * otro.real - self.real * otro.imaginaria) / denominador
        return CalculadoraCompleja(nueva_real, nueva_imaginaria)

# Ejemplo de uso
num1 = CalculadoraCompleja(3, 4)
num2 = CalculadoraCompleja(1, 2)

resultado_suma = num1.suma(num2)
resultado_resta = num1.resta(num2)
resultado_multiplicacion = num1.multiplicacion(num2)
resultado_division = num1.division(num2)

print(f"Suma: {resultado_suma}")
print(f"Resta: {resultado_resta}")
print(f"Multiplicación: {resultado_multiplicacion}")
print(f"División: {resultado_division}")
