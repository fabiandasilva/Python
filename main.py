
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

""" Repetir pero para la expresión que permite saber si un número es par y menor a 10. """

""" numero = int(input("Ingrese un numero:"))

def es_par_menor_10(numero):
    if numero % 2 == 0 and numero < 10:
        return print("Es par y menor a 10")
    else:
        return print("No es par o no es menor a 10")
    
es_par_menor_10(numero) """



""" 4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
el mismo número sin considerar el signo.
Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4). """


""" numero = int(input("Ingrese un numero: "))
def valor_absoluto(numero):
    if numero < 0:
        return numero * -1
    else:
        return numero

print(valor_absoluto(numero)) """


""" Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
a ser representado con una letra: R para piedra, P para papel y T para tijera.
a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
la jugada para ganarle. Por ejemplo:
> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
> P
> Tijera. ¡Te gané!
ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
que hacer (en este caso ingresar alguna de las tres letras).
b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
(distinta de R, P o T). """

""" juego = str(input("Ingrese piedra (R), papel (P) o tijera (T): "))

def juego_piedra_papel_tijera(juego):
    if juego == "R" or "r":
        return   print("Papel, te gane!")
    elif juego == "P" or "p":
        return  print ("Tijera, te gane!")
    elif juego == "T" or "t":
        return print ("Piedra, te gane!")
    else:
        print("No vale!")

juego_piedra_papel_tijera(juego) """



""" 6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”.
Extra: ¿Cómo harían para que el programa quede generalizado para cualquier límite, a elección del
usuario, y no solo para 100?. """

""" ingrese_primer_numero = int(input("Ingrese el primer número "))
ingrese_segundo_numero = int(input("Ingrese el segundo número "))
suma = ingrese_primer_numero + ingrese_segundo_numero
limite = int(input("Establezca el limite "))

def pasa_el_limite(suma, limite):
    if suma > limite:
        return print(f"La suma es {suma} y supera el limite ")
    else:
        return print(f"La suma es {suma} y no supera el limite ")

pasa_el_limite(suma, limite) """

#7. Se tienen letras para representar las estaciones del año:
#● V para verano
#● O para otoño
#● I para invierno
#● P para primavera
#Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
#decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
#ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
#B, V e I


""" letras = str(input("Ingrese una letra V, O, I o P: "))

def estacion_del_anio(letras):
    letras = letras.upper()
    if letras == "V":
    elif letras == "O":
        return print("Estas en la estacion de Otoño ")
    elif letras =="I":
        return print("Estas en la estacion Invierno ")
    elif letras =="P":
        return print("Estas en la estacion de Primavera ")
    else:
        return print("Por favor ingresa alguna de las opciones") 
    

estacion_del_anio(letras) """

""" Estructuras de control iterativas """

""" 8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
iterativa for. """
    
    
""" numero_inicial = int(input("Ingrese un numero: "))

for numero in range(numero_inicial, 10):
    print(numero) """

""" 9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
número entero e imprima por pantalla la tabla de ese número del 1 al 10. """

""" numero = int(input("Ingrese un numero y aprendamos la tabla de multiplicar: "))

def tabla_de_multiplicar(numero):
    for factor in range(1, 11):
        resultado = numero * factor
        print(f"{numero} x {factor} = {resultado}")
        
        
tabla_de_multiplicar(numero) """



""" 10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
cantidad de veces. """

""" cantemos =int(input("Ingrese la cantidad de veces que quiere que cantemos: "))

def cantemos_cumple(cantemos):
    for cancion in range(1, cantemos):
        print("Que los cumplas feliz")

cantemos_cumple(cantemos)  """


""" 11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos
pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30: """
    
""" precio_pagar = int(input("Ingrese el precio a pagar: "))
monto = int(input("Ingrese el monto: "))
deuda = precio_pagar - monto

def cobrar(monto, deuda):
    while deuda > 0:
        print(f"Debe pagar {deuda}")
        monto = int(input("Ingrese el monto: "))
        deuda = deuda - monto
    print("Gracias por su compra")

cobrar(precio_pagar, monto, deuda)  """

""" 12. Escribir código que recorra los números del 1 al 20 y determine para cada uno si es par o impar,
imprimiendo un mensaje por pantalla en cada caso. Es decir, el output esperado sería: """
    
""" for i in range(1, 21):
  if i % 2 == 0:
       print(f"{i} Es par ")
  else:
       print(f"{i} No es par ") """

""" 13. Se tiene una máquina de sacar juguetes que funciona cuando se ingresa una determinada cantidad de
fichas, y se quiere hacer una función que imite ese comportamiento.

a. Hacer una función que reciba un número que represente el precio de la máquina, e imprima
por pantalla “Ingresá x fichas para comenzar” hasta que se hayan ingresado esa cantidad de
letras F (que representan una ficha), y luego “¡A jugar!” cuando se hayan ingresado todas las
fichas necesarias. Por ejemplo, si la función recibe 3, debería tener el siguiente
comportamiento: """



""" precio_maquina = int(input("Ingrese el precio de la maquina: "))


def juego(precio_maquina):
    ficha_ingresada = 0
    while precio_maquina > ficha_ingresada:
        ficha  = input("Ingrese una ficha (F)")
        if ficha.upper() == "F":
            ficha_ingresada +=1
            fichas_restantes = ficha_ingresada - precio_maquina
            print(f"Faltan {fichas_restantes} para comenzar")
        else:
            print("Por favor solamente ingrese fichas reales (F)")            
    print("A jugar!")

juego(precio_maquina) """
        
 

""" 14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
ingresado. """
    
    
""" def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def numeros_primos_hasta_n(n):
    for i in range(2, n + 1):
        if es_primo(i):
            print(i)
            
numero_ingresado = int(input("Ingrese un número entero: "))
print(f"Números primos entre 0 y {numero_ingresado}:")
numeros_primos_hasta_n(numero_ingresado)
 """
  
  
  
#Familiarización con secuencias

""" 1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número
5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0. """
 
""" lista = [1,2,3,4,5,6,7,8,9,10] 
print(lista[4]) """
       
""" 2. Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla. """

""" print(len(lista)) """


""" Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo. """


""" lista_numeros_random =[55, 20, 100, 1, 0, 99, 1000, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(max(lista_numeros_random))
print(min(lista_numeros_random)) """



""" 9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la
siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos
tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo. """


""" libreria = ["El principito", "It", "Sherlock Holmes", "It"]

def libros_repetidos(libreria): 
    for libro in libreria:
        print(f"El libro {libro} se repite {libreria.count(libro)} veces")
    
libros_repetidos(libreria) """


""" 10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
números elevados al cuadrado. """


""" lista = [1,2,3,4,5,6,7,8,9,10]

def elevar_al_cuadrado(lista):
    for numero in lista:
        print(numero ** 2)

elevar_al_cuadrado(lista) """

""" 11. Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”,
“escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”,
“escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar
la frase. (ver funciones de listas y strings). """


lista_palabras = ["entender", "pueden", "humanos", "los", "que", "código", "escriben", "programadores", "buenos", "Los", "entiende.", "computadora", "una", "que", "código", "escribe", "tonto", "Cualquier"]

def unir_palabras(lista_palabras):
    """ Utilizo el metodo reverse para invertir el orden de la lista """
    lista_palabras.reverse()
    print(lista_palabras)
    """ Utilizo el metodo join para unir las palabras de la lista """
    lista_palabras = " ".join(lista_palabras)
    print(lista_palabras)
    
    
    
unir_palabras(lista_palabras)
    
    