# Esto es un comentario en Python
"""
Esto es un comentario 
de diversas lineas
"""
mensaje = "Hola mundo"
print (mensaje)

"""
Unica diferencia con otros lenguajes 
a la hora de declarar variables
las variables booleanas se declaran con True o False
¡¡¡La primera en mayúscula siempre!!!
"""
verdadero = True
falso = False

"""
También puedes asignar el mismo valor a múltiples variables
en una sola línea utilizando el operador de asignación múltiple:
"""
a = b = c = 10
# Esto significa que tanto a como b como c tendrán un valor de 10
print ("El valor de a es:",a)
print ("El valor de b es:",b)
print ("El valor de c es:",c)

# Las variables pueden declararse de siguientes formas
edad = 10
nombre_completo = "Miguel"
año_nacimiento = 2003
_es_mayor_edad = True

# Operadores lógicos, viniendo de PHP(|,||,&,&&,!) en este lenguaje cambian las sentencias
resultado_and = (a == b) and (b == 10) # True
resultado_or = (a > 15) or (b == 10) # True
resultado_not = not (a < 5) #False

#ESTRUCTURAS DE CONTROL
#a = 5
if a == b:
    print("Los dos numeros tienen el mismo valor que es:",a)
else:
    print("El valor de a que es:",a," es disinto al de b que es:",b)

# Ejemplo de elif
# Se pueden poner tantos elif como condiciones queramos poner(no es recomendable realizar un número excesivo condiciones en un mismo bloque)
if edad > 18:
    print ("ERES MAYOR DE EDAD!!")
elif edad <= 18:
    print ("ERES MENOR DE EDAD!!!")
else:
    print("TU EDAD NO PUEDE SER INFERIOR A 0!")

# BUCLES
# Bucle for
frutas = ["manzana","pera","limon"]
"""
 La estructura es la siguiente: 
 for [índice] in [array/vector]
"""
for fruta in frutas:
    print(fruta)

# Bucle While
contador = 0

while contador <= 5:
    print(contador)
    contador += 1

# LISTAS
frutas = ["manzana","pera","limon"]
# Para acceder a los elementos de una lista/array/vector
print(frutas[0]) # Imprime la primera posicion del array es decir manzana
print(frutas[1]) # Imprime la segunda posicion del array es decir pera
print(frutas[2]) # Imprime la tercera posicion del array es decir limon
# Tambien podemos imprimir los elementos desde el final
print(frutas[-1]) # Imprime la tercera posicion del array es decir limon
print(frutas[-2]) # Imprime la segunda posicion del array es decir pera
print(frutas[-3]) # Imprime la primera posicion del array es decir manzana
# Métodos más utilizados en las listas
# El método append nos permite concatenar elementos en el array
frutas.append("frambuesa")
print(frutas) # Imprimira toda la lista incluyendo el ultimo elemento concatenado que es frambuesa
# El método insert nos permite insertar en la posicion que gustemos un elemento a la lista
frutas.insert(1,"uva")
print(frutas) # Imprime todos los elementos pero la uva apareceria en la segunda posicion
# El método remove para eliminar elementos de la lista por su nombre
frutas.remove("uva")
print(frutas) # se deben mostrar todos los elementos anteriores excepto la uva
# El método pop, nos permite eliminar un elemento y guardarlo para mostrarlo como elemento eliminado recientemente
fruta_eliminada = frutas.pop(2)
print(frutas) # se deben de mostrar todos los elementos anteriores excepto el limon
print("La fruta eliminada fue el",fruta_eliminada) # nos muestra le fruta eliminada con el método utilizado
# El método sort que nos permite ordenar la lista por orden alfabetico
frutas.sort()
print(frutas) 
# El método reverse que nos permite ver la lista en el sentido contrario
frutas.reverse()
print(frutas)

# LISTA DE COMPRESION
lista_numerica = [1,2,3,4,5,6,7,8,9,10]
# La expresión x ** 2 eleva cada elemento al cuadrado, y la condición if x % 2 == 0 filtra solo los números pares.
cuadrados = [x ** 2 for x in lista_numerica if x % 2 == 0]
print(cuadrados) # Imprime los numeros cuadrados pares

# TUPLAS
# Las tuplas a diferencia de las listas son inmutables, es decir no se pueden modificar una vez creadas
punto = (3,4)
print(punto[0]) # imprime 3
print(punto[1]) # Imprime 4

# Métodos
tupla_numerica = (1,1,1,2,3,7,8,6,6,2,6)

# El método count devuelve el numero de veces que aparece un elemento en la tupla
print ("El numero 1 aparece en la tupla una cantidad de ",tupla_numerica.count(1)," veces.")
# El método index devuelve la posicion de la primera aparicion del elemento en la tupla 
print ("El numero 6 aparece por primera vez en la posicion:",tupla_numerica.index(6))
# El método len devuelve la longitud o tamaño de la tupla
print ("La longitud de la tupla_numerica es de",len(tupla_numerica),"numeros")

# DICCIONARIOS
# Para crear diccionarios se deben utilizar llaves y separar ls claves de los valores con dos puntos
# nombre_diccionario = {"clave":valor,"clave":valor,"clave":valor}
persona = {"nombre":"José","apellido":"Martínez","edad":22,"ciudad":"Almeria"}
print("Muy buenas, mi nombre es",persona["nombre"],persona["apellido"],", tengo",persona["edad"],"años, nacido en ", persona["ciudad"])
# Métodos
# El método keys devuelve una vista de todas las claves del diccionario(solo claves)
print(persona.keys())
# El método values devuelve una vista unica de los valores del diccionario
print(persona.values())
# El método items devuelve una vista de todos los pares clave-valor del diccionario
print(persona.items())
# El método update utiliza los pares clave-valor de otro diccionario para actualizar el que estamos usando
persona.update({"estudios":"Desarrollo de Aplicaciones Web", "siglas_estudios":"DAW"})
print(persona)
# CONJUNTOS
# Para crear conjuntos se puede utilizar llaves({}) o el metodo set
frutas = {"limon","pera","manzana"}
numeros = set([1,2,3,4,5,6,7,8,9,10])
# Los conjuntos admiten operaciones matemáticas de conjuntos como la union,interseccion,diferencia y la diferencia simetrica
conjunto1 = {1,2,3}
conjunto2 = {3,4,5}
# Utilizamos la barra vertical para crear la union entre dos conjuntos
# [conjunto_ej1] | [conjunto_ej2]
union = conjunto1 | conjunto2
print(union)
# Para el caso de la interseccion utilizamos la letra &
interseccion = conjunto1 & conjunto2
print(interseccion)
# Continuamos con la diferencia, para este tipo de operacion utilizamos el simbolo -
diferencia = conjunto1 - conjunto2
print(diferencia)
# Mientras que la diferencia simetrica funciona con el simbolo ^
diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)

# Métodos
# Los conjuntos cuentan con diferentes tipos de métodos
# El primero de ellos el método add que agrega un elemento al conjunto
frutas_verano = {"melon","sandia","brevas"}

frutas_verano.add("higos")
print(frutas_verano)
# El método remove, que elimina un elemento del conjunto
frutas_verano.remove("higos")
print(frutas_verano)
# El método discard, este método elimina un elemento del conjunto si se encuentra en el sino no hace nada
frutas_verano.discard("manzana")
print(frutas_verano)
# El método clear, como su nombre indica limpia por completo el conjunto y lo muestra vacio
frutas_verano.clear()
print(frutas_verano)
