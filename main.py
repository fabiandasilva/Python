
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

""" 11. Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra). """

""" entrada = str(input("Escribi tu palabra: "))

def medir_longitud_palabra(entrada):  
    entrada += "5"  
    print(len(entrada))

medir_longitud_palabra(entrada)
 """





""" 12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida
de Python). """

""" entrada = str(input("Escribi tu palabra: "))

def borrar_a(entrada):
    entrada = entrada.replace("a", "")
    print(entrada)
 
borrar_a(entrada) """

 


""" Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
bool e imprimirla por pantalla para ver su valor. """

""" valor1 = int(input("Escribi tu 1er numero: "))
valor2 = int(input("Escribi tu 2do numero: "))
variable_booleano = True

def is_bigger(valor1, valor2, variable_booleano):
    valor1 = valor1
    valor2 = valor2
    if valor1 > valor2:
        print(f"El resultado es {variable_booleano}")
    else:
        print(False)
 """
 
 
""" def rel(a, b):
     if a > b:
         return True
     else:
         return False
num1 = input("numero uno ")
num2 = input("numero dos ")

print(rel(num1, num2)) """
     
""" def es_mas_grande(numero1, numero2):
    return numero1 > numero2

# Obtener los números del usuario
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Obtener el resultado de la función
resultado = es_mas_grande(num1, num2)

# Imprimir el valor del resultado
print("¿El número 1 es más grande que el número 2?", resultado)

 """

""" numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

def es_mas_grande(numero1, numero2):
    if numero1 > numero2:
        return True
    else:
        return False
resultado = es_mas_grande(numero1, numero2)

print(resultado) """


""" 2. Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal """
""" letra = str(input("Ingrese una letra: "))

def es_vocal(letra):
    if letra == "a" or letra =="e" or letra =="o" or letra =="u" or letra =="i":
        return True
    else:
        return False
    
print(es_vocal(letra)) """

