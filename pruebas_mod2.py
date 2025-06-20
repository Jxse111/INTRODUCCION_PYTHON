# FUNCIONES
# En Python las funciones se denominan con la palabra reservada def
def bienvenida():
    print ("Bienvenido/a!")

# Realizamos una llamada a la función y se nos muestra lo que devuelve esta funcion
bienvenida()

# Como toda funcion puede recibir o no argumentos 
def bienvenida_saludo(nombre):
    print("Bienvenido,",nombre)

bienvenida_saludo("José")

# También podemos declarar una variable en la que almacenemos el nombre para pasarlo por los parametros de la funcion
nombre = "Miguel"
bienvenida_saludo(nombre)

# Las funciones pueden devolver o retornar datos no solo imprimir por pantalla
def suma (a,b):
    return a + b 
resultado = suma(3,4)
print ("El resultado de la suma de 3 + 4 es",resultado)

# También contamos con funciones de tipo lambda o anónimas
cuadrado = lambda x: x ** 2
print(cuadrado(5)) # Imprime 25

# Diferencias entre variables locales de una funcion y variables globales
# las variables locales son aquellas variables que se instancian dentro de una funcion para el uso de estas dentro de la misma 
# Mientras que las variables globales son aquellas variables que han sido definidas fuera del bloque de funcion y se pueden llamar en cualquier parte del programa

def funcion():
    variable_local = 10
    print(variable_local)

variable_global = 20

def funcion2():
    print(variable_global)

funcion()
funcion2()
print(variable_global)
#Como podemos observar si descomentamos la impresion de la variable local nos
# da un error de que esta variable no esta definida ya que no es una variable global sino local
#print(variable_local)

# Y por último tenemos funciones creadas por el usuario
# Estas se deben documentar de forma correcta para el uso de otros usuarios 
def precioConIva(precio,IVA=1.21):
    """
    Calcula el precio de un producto con IVA

    Argumentos:
    precio (float): el precio del producto
    IVA (float)(OPCIONAL): el IVA aplicado al precio del producto

    Returns:
    float : el precio con el IVA asignado
    """
    return precio * IVA

# Funciones con número variable de argumentos
# Este tipo de funciones se accionan agregando el operador * antes del nombre del parametro

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
        return total
    
print(suma_variable(1,2,3)) # Imprime 6
print(suma_variable(4,5,6,7)) # Imprime 22

# MANEJO DE EXCEPCIONES 
# Como en otros lenguajes los errores se capturan con las palabras reservadas
# Try - catch
# En este caso en Python la sentencia catch es renombrada como Except(Exception)
try:
    # Código que puede generar una excepción
    resultado = 10 / 0 # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: La division es por cero, no se puede realizar dicha operacion.")

# También contamos con un bloque opcional llamado finally, que se ejecuta siempre, da igual si hay excepcion o no
#try:
    # Código que puede generar una excepción
#    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
#except FileNotFoundError:
#    print("Error: Archivo no encontrado")
#finally:
#    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción


# Por último tenemos una forma única de crear excepciones personalizadas
def esMayor(edad):
    if edad >= 18:
        print("Eres mayor de edad")
    elif edad < 18 and edad >= 1:
        print("Eres menor de edad")
    else: 
        raise Exception("Tu edad no puede ser 0")
try:
    esMayor()
except Exception as ex:
    print("ERROR:",ex) 
# Nos debe saltar el error en la linea en la que se ejecuta la funcion mostrando que el parametro no puede ser 0
#esMayor(0)


# ENTRADAS/SALIDAS
# Para que el usuario que ejecute el programa pueda introducir datos con el teclado
# Debemos de crear una variable input(entrada), la cual guardara los datos introducidos por teclado
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
edad = int(edad)
print("Hola,",nombre,"")
print("Tienes",edad,"años.")
esMayor(edad)
# Para mostrar información en pantalla utilizamos la funcion print nos permite tomar uno o mas argumentos y los muestra por consola
# podemos utilizar f-string para formatear cadenas e incorporar variables dentro de una misma cadena
print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# LECTURA DE ARCHIVOS
# Al igual que en otros lenguajes, Python nos permite leer el contenido de archivos usando diversos métodos
archivo = open ("info.txt","r") # r es el modo de lectura proviene de la palabra read
contenido = archivo.read() #Abre el archivo info.txt y nos muestra por consola el contenido de este
print(contenido)
archivo.close()

# ESCRITURA DE ARCHIVOS
# En este caso lo que vamos a hacer es escribir sobre el archivo info.txt
archivo = open("info.txt","w") # w es el modo de escritura proviene de la palabra write
archivo.write("Un usuario estuvo escribiendo en este archivo!")
archivo.close()
# Si volvemos a leer el archivo se nos debe mostrar lo siguiente
print(contenido)
# Tambien podemos utilizar la palabra reservada with para manejar la apertura y cierre de archivos de manera automatica
with open("datos.txt","w") as archivo:
    archivo.write("Segunda edición del archivo editado")

# IMPORTAR MÓDULOS / IMPORTS
# Como en otros lenguajes, Python permite importar modulos de las librerias del lenguaje
# Por ejemplo el mas famoso modulo math, para operaciones matematicas
import math
resultado = math.sqrt(25) # Esta funcion interna del modulo math calcula la raiz cuadrada del número que le pasemos por parámetros
print(resultado) # Imprime 5.0

# También se puede importar funciones especificas para no importar el modulo completo
from math import trunc

resultado = trunc(2.5)
print(resultado) # Imprime 2

# Otras bibliotecas son Random, Datetime
import random
import datetime

numero_aleatorio = random.randint(1,10)
print(numero_aleatorio) # Cada vez que lo ejecutemos devolvera un numero aleatorio del 1 al 10

fecha_actual = datetime.datetime.now()
print("Fecha del dia de hoy:",fecha_actual) # Imprimer la fecha y hora actual

# CREACION DE MÓDULOS PROPIOS
# En python podemos crear módulos propios, simplemente creamos un nuevo archivo para el modulo y dentro de este definimos funciones,clases,variable...
from modulo_controladores import modulo_funciones_generales,modulo_funciones_persona
modulo_funciones_generales.saludar(nombre)
resultado_suma = modulo_funciones_generales.calcular_suma(5,10)
print (f"El resultado de la suma de 5 + 10 es {resultado_suma}")
print(modulo_funciones_persona.esMayor(18))