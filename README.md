# Calculadora con Programación Orientada a Objetos

Este proyecto implementa una calculadora en Python utilizando los cuatro pilares de la Programación Orientada a Objetos (POO): **Abstracción, Encapsulamiento, Herencia y Polimorfismo**.

## 1. Abstracción
La abstracción nos permite definir clases que representan conceptos generales, ocultando los detalles internos y exponiendo solo lo necesario.

### Ejemplo en `calculadora.py`:
```python
class Calculadora:
    def __init__(self):
        self.__resultado = 0
        self._operacion = ''
    
    def sumar(self, a, b):
        self._operacion = 'Suma'
        self.__resultado = a + b
        return self._mostrar_resultado(a, b)
```
Aquí, la clase ``Calculadora`` proporciona métodos para realizar operaciones matemáticas sin exponer cómo almacena o maneja los resultados internamente. El usuario solo necesita llamar a sumar(), sin preocuparse por los detalles internos.

### Ejemplo de uso en `main.py`:
```python
calculadora_1 = Calculadora()
print(calculadora_1.sumar(5, 3))
```
#### Salida esperada:
```
Suma: 5 y 3 = 8
```

---

## 2. Encapsulamiento
El encapsulamiento protege los atributos y métodos internos de la clase, evitando modificaciones accidentales.

### Ejemplo en `calculadora.py`:
```python
class Calculadora:
    def __init__(self):
        self.__resultado = 0  # Atributo privado
        self._operacion = ''  # Atributo protegido
```
El atributo ``__resultado`` no es accesible directamente desde fuera de la clase debido a la convención de doble guion bajo en Python. Sin embargo, Python permite acceder a él mediante self._Calculadora__resultado, aunque esto no es recomendable ya que rompe el encapsulamiento.

---

## 3. Herencia
La herencia permite crear nuevas clases basadas en una clase existente, reutilizando su funcionalidad.

### Ejemplo en `factorial_poo.py`:
```python
from calculadora import Calculadora

class CalculadoraFactorial(Calculadora):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero
        self._operacion = 'factorial'
        self._Calculadora__resultado = 1
```
`CalculadoraFactorial` hereda de `Calculadora`, aprovechando su estructura y modificándola para calcular factoriales.

### Ejemplo de uso en `main.py`:
```python
calculadora_factorial = CalculadoraFactorial(5)
print(calculadora_factorial.calcular())
```
#### Salida esperada:
```
El factorial de 5 es: 120
```

---

## 4. Polimorfismo
El polimorfismo permite redefinir métodos en una subclase, cambiando su comportamiento.

### Ejemplo en `factorial_poo.py`:
```python
class CalculadoraFactorial(Calculadora):
    def calcular(self):
        for i in range(self.numero):
            self._Calculadora__resultado = self._multiplicar(self._Calculadora__resultado, i + 1) 
        return self._mostrar_resultado()

    def _mostrar_resultado(self):
        return f'El {self._operacion} de {self.numero} es: {self._Calculadora__resultado}'
```
En este caso, `CalculadoraFactorial` sobrescribe `_mostrar_resultado()` de `Calculadora` para adaptar la salida al cálculo del factorial que ahora no necesita los argumentos que originalmente sí.

### Ejemplo de uso en `main.py`:
```python
calculadora_factorial_2 = CalculadoraFactorial(6)
print(calculadora_factorial_2.calcular())
```
#### Salida esperada:
```
El factorial de 6 es: 720
```
