"""
    Fecha: Miércoles 02 de Noviembre del 2022
    Nombre: Harry Enrique Bodán Navarro
    Versión del programa: 1.0
    Clase: Algoritmo y Estructura de Datos
    Grupo: B119
    Módulo Structures: Contiene la clase principal "Account"
"""

class Account:

    def __init__(self, name, cardNumber, pin):
        self.Name = name
        self.CardNumber = cardNumber
        self.Pin = pin
        self.Amount = 0

    def __str__(self):
        return f"""Nombre: {self.Name}
Número de tarjeta: {self.CardNumber}
Pin: ****
Monto disponible: {self.Amount}
"""