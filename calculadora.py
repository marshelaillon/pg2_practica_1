import math

# Clase base que representa una calculadora simple (Abstracción)
class Calculadora:
  def __init__(self, a, b):
    self.__resultado = 0
    self.operacion = ''
    self.a = a
    self.b = b

  def _mostrar_operacion(self):
    return f'{self.operacion}: {self.a} y {self.b} = {self.__resultado}'
  
  def mostrar_operaciones(self):
    return f'{self._sumar()}\n{self._restar()}\n{self._multiplicar()}\n{self._dividir()}\n'

  def _sumar(self):
    self.operacion = 'Suma'
    self.__resultado = self.a + self.b
    return self._mostrar_operacion()
  
  def _restar(self):
    self.operacion = 'Resta'
    self.__resultado = self.a - self.b
    return self._mostrar_operacion()

  def _multiplicar(self):
    self.operacion = 'Multiplicar'
    self.__resultado = self.a * self.b
    return self._mostrar_operacion()
  
  def _dividir(self):
    self.operacion = 'Dividir'
    self.__resultado = self.a / self.b
    return self._mostrar_operacion()

calculadora_1 = Calculadora(10, 10)
calculadora_2 = Calculadora(20, 15)
print(calculadora_1.mostrar_operaciones())
print(calculadora_2.mostrar_operaciones())
