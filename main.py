
#1. Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
#   Recordá que podés usar las funciones input (para solicitar información) y print para mostrar
#   información.

""" valorNumero = int(input("Ingrese un numero: ")) """
"""  """
""" print("El numero ingresado es: ", valorNumero) """

""" 2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
● la suma de ambos números
● la resta de ambos números
● la multiplicación de ambos números
● la división entera de ambos números
● el resto
Más adelante podríamos crear nuestra propia calculadora :) """

""" valor_uno = int(input("Ingrese el primer valor"))
valor_dos = int(input("Ingrese el primer valor"))

suma = valor_uno + valor_dos

print(suma) """


""" 3. Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
mensaje que indique el resultado.
Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
dejamos a ustedes el cómo. """



""" entrada = int(input("Ingrese un numero entero "))

if (entrada % 2 == 0) : 
    print("Es un numero par ") 
    
else:
    print ("Es un numero impar ")
 """


""" 4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
el usuario en el año ingresado """

""" año_nacimiento = int(input("Ingrese su año de nacimiento "))
nuevo_año= int(input("Ingrese un año "))

respuesta = nuevo_año - año_nacimiento

print(f"la edad que tenias en el año ingresado es: {respuesta}") """


""" 5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
Es muy común usar variables para acumular valores. """


""" valor_uno =int(input("Ingrese el primer valor "))
valor_dos =int(input("Ingrese el segundo valor "))
valor_tres =int(input("Ingrese el tercero valor "))
valor_cuatro =int(input("Ingrese el cuarto valor "))
valor_cinco =int(input("Ingrese el quinto valor "))

promedio = (valor_uno + valor_dos + valor_tres + valor_cuatro + valor_cinco )/ 5

print(f"El promedio es : {promedio}")  """


""" Crear una función que reciba un número y muestre el anterior y el siguiente. """


""" def funcion (a):
    anterior =a -1
    siguiente = a +1
    print(f"El numero anterior es {anterior} y el siguiente es {siguiente}")


funcion(100) """


""" Crear una función que una un string y un entero, ambos dentro de un string """

""" string = str(input("Ingrese un string ")) 
entero = int(input("Ingrese un entero "))

def funcion_con_string_entero (string, entero):
    print(f"Aca va el string {string} y aca esta el entero {entero}")

funcion_con_string_entero(string, entero) """


""" 8. Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente. """
""" a = int(input("Ingrese un valor "))

def cuenta (a):
    cociente = a / 2
    resto = a % 2 
    print(f"Cociente: {cociente} y resto: {resto}")

cuenta(a) """