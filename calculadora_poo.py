class Calculadora:
  def __init__(self):
    self.__resultado = 0
    self._operacion = ''
    
  def sumar(self, a, b):
    self._operacion = 'Suma'
    self.__resultado = a + b
    return self._mostrar_resultado(a, b)

  def restar(self, a, b):
    self._operacion = 'Resta'
    self.__resultado = a - b
    return self._mostrar_resultado(a, b)

  def _multiplicar(self, a, b):
    return a * b

  def multiplicar(self, a, b):
    self._operacion = 'Multiplicación'
    self.__resultado = self._multiplicar(a, b)
    return self._mostrar_resultado(a, b)
  
  def dividir(self, a, b):
    self._operacion = 'División'
    self.__resultado = a / b
    return self._mostrar_resultado(a, b)

  def _mostrar_resultado(self, a, b):
    return f'{self._operacion}: {a} y {b} = {self.__resultado}'