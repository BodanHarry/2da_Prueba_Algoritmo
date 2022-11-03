"""
    Fecha: Miércoles 02 de Noviembre del 2022
    Nombre: Harry Enrique Bodán Navarro
    Versión del programa: 1.0
    Clase: Algoritmo y Estructura de Datos
    Grupo: B119
    Módulo Functions: Funciones necesarias para que funcione el programa
"""

import os
import time

from Structures import Account as acc

listAccounts = []

def add_accounts(name, numberCard, pin):
    """Añade objetos de tipo Accounts en el arreglo de 
    cuentas"""

    account = acc(name,numberCard, pin)
    listAccounts.append(account)

def show_list_accounts():
    """Muestra los objetos de tipo Accounts almacenados 
    en el arreglo de cuentas"""

    for element in listAccounts:
        print("")
        print(element)
        print("-" * 50)

def progress_bar(segment, total, long):
    """Prepara un estilo de barra (Función estética)"""

    average = segment / total
    complete = int(average * long)
    remaining = long - complete
    bar = f"[{'-' * complete}{'#' * remaining}{average: .00%}]"
    return bar

def validate_account(account, pin):
    """Valida si existe el patrón account-pin en algún 
    elemento de la lista, para iniciar sesión"""

    for element in listAccounts:
        if account == element.CardNumber and element.Pin == pin:
           return True

def validate_quantity(quantity):
    """Valida si la cantidad recibida es múltipo de 100"""

    if quantity % 100 == 0:
        return True
    else:
        return False

def validate_amount(amount, quantity):
    """Valida si la cantidad ingresada no es mayor al monto 
    de la cuenta"""

    if quantity <= amount:
        return True
    else:
        return False

def deposit_money(account):
    """Deposita la cantidad ingresada al depósito si 
    se cumplen las condiciones de cantidad"""
    
    try:
        for acc in listAccounts:
            if account == acc.CardNumber:
                quantity = int(input("Cantidad a depositar: "))
                validatorQuantity = validate_quantity(quantity)
                if(validatorQuantity):
                    acc.Amount = acc.Amount + quantity;
                else:
                    print("No se pudo realizar la transacción")
                    os.system("PAUSE")
    except:
        print("Error al depositar dinero")

def withdrawal_money(account):
    """Retira la cantidad ingresada al depósito si 
    se cumplen las condiciones de cantidad y monto"""

    try:
        for acc in listAccounts:
            if account == acc.CardNumber:
                quantity = int(input("Cantidad a retirar: "))
                validatorQuantity = validate_quantity(quantity)
                validatorAmount = validate_amount(acc.Amount, quantity)
                if(validatorQuantity and validatorAmount):
                    acc.Amount = acc.Amount - quantity;
                else:
                    print("No se pudo realizar la transacción")
                    os.system("PAUSE")
    except:
        print("Error al retirar dinero")

def show_amount(account):
    """Muestra el saldo disponible de la cuenta en la
    que la sesión esté iniciada"""

    try:
        for acc in listAccounts:
            if account == acc.CardNumber:
                print("Su estado de cuenta es: ", acc.Amount)
                os.system("PAUSE")
    except:
        print("Error al retirar dinero")

def options():
    """Muestra las opciones que tiene el usuario y recibe
    la respuesta del usuario a estas"""

    os.system("cls")
    print("Bienvenido a tu banca")
    print("Operaciones que puede realizar:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Ver Saldo")
    print("4. Salir")
    op = int(input("Opción: "))
    return op
    
def menu(account):
    """Segun la opción ingresada, evalúa la función a la
    cuál dirigirse"""

    op = 0
    while(op!=4):
        op = options()
        if(op==1): deposit_money(account)
        elif(op==2): withdrawal_money(account)
        elif(op==3): show_amount(account)
        elif(op==4): print("Adios")
        else: 
            print("Opción incorrecta")
            os.system("PAUSE")


def login_options():
    """Muestra la opción iniciar sesión o salir y recopila
    la respuesta del usuario"""

    os.system("cls")
    print("1. Iniciar sesión")
    print("2. Salir")
    op = int(input("Digite su opción: "))
    return op

def main():
    """Según la respuesta que recibe de login_options(),
    ejecuta las distintas funcionalidades de la plataforma,
    además, mientras no se haya iniciado sesión, no redigire
    al usuario a ningún lado hasta que salga completamente"""

    op = login_options()
    while(op != 2):
        if (op==1):
            os.system("cls")
            account = input("Digite su número de cuenta: ")
            pin = input("Digite su pin: ")
            for i in range(31):
                time.sleep(0.05)
                print(progress_bar(i, 30, 30), end = "\r")
            answer = False
            answer = validate_account(account, pin)
            print("")
            if(answer):
                menu(account)
            else:
                print("Credenciales incorrectas")
                os.system("PAUSE")
        else:
            print("Opción inválida")
            os.system("PAUSE")
        op = login_options()   