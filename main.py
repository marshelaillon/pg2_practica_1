from calculadora import Calculadora
from factorial_poo import CalculadoraFactorial

calculadora_1 = Calculadora()
print(calculadora_1.sumar(5, 3))
print(calculadora_1.restar(10, 4))

calculadora_2 = Calculadora()
print(calculadora_2.multiplicar(10, 9))
print(calculadora_2.dividir(100, 5))

calculadora_factorial = CalculadoraFactorial(5)
print(calculadora_factorial.calcular())

calculadora_factorial_2 = CalculadoraFactorial(6)
print(calculadora_factorial_2.calcular())