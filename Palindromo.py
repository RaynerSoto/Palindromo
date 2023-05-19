import string
import time
def palindrmo():
    entrada = input('Ingrese la palabra para ver si es un palidromo\n')
    valor = list(entrada.lower())
    valor.reverse()
    value = ''.join(valor)  # Convertir un arreglo en un string con un separador ''
    if (entrada.lower().replace(' ', '') == value.lower().replace(' ', '')):  # Eliminar los elementos en blanco
        print('Es palídromo')
    else:
        print('No es palídromo')
