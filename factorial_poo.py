from calculadora import Calculadora

class CalculadoraFactorial(Calculadora):
  def __init__(self, numero):
    super().__init__()
    self.numero = numero
    self._operacion = 'factorial'
    self._Calculadora__resultado = 1

  def calcular(self):
    for i in range(self.numero):
      self._Calculadora__resultado = self._multiplicar(self._Calculadora__resultado, i + 1) 
    return self._mostrar_resultado()
  
  def _mostrar_resultado(self):
    return f'El {self._operacion} de {self.numero} es: {self._Calculadora__resultado}'