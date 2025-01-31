# %% [markdown]
# # NOTEBOOK 02 - Tipos de datos y estructuras de datos
# ## Fundamentos de Programación: Tipos de Datos, Variables y Operaciones Básicas
# ### Nombre del estudiante: 
# 
# ---
# 
# ## 1. Tipos de Datos en Python
# 
# ### Teoría
# Los tipos de datos en Python determinan el tipo de valor que se puede almacenar y manipular. Los más comunes son:
# 
# - **Enteros (`int`)**: Números sin parte decimal.
# - **Flotantes (`float`)**: Números con parte decimal.
# - **Cadenas de texto (`str`)**: Secuencias de caracteres.
# - **Booleanos (`bool`)**: Valores lógicos que pueden ser `True` o `False`.
# 
# #### Comparaciones:
# - Los enteros representan números sin decimales, mientras que los flotantes incluyen decimales.
# - Las cadenas de texto permiten almacenar y manipular texto.
# - Los booleanos permiten realizar comparaciones lógicas en el código.
# 
# ### Ejemplos
# ```python
# # Ejemplos de tipos de datos
# numero_entero = 10  # Tipo entero
# numero_flotante = 10.5  # Tipo flotante
# cadena_texto = "Hola, Python!"  # Tipo cadena
# valor_logico = True  # Tipo booleano
# 
# # Imprimir los tipos de cada variable
# print(type(numero_entero))
# print(type(numero_flotante))
# print(type(cadena_texto))
# print(type(valor_logico))
# ```
# 
# ## Ejercicios 
# 
# 1. Declara una variable de tipo entero y asigna el valor *25*. Luego, imprime su tipo.

# %%
#Respuesta


# %% [markdown]
# 2. Declara una variable de tipo flotante con el valor *3.1416*. Imprime su tipo.
# 

# %%
#Respuesta

# %% [markdown]
# 3. Crea una variable es_estudiante que almacene un valor booleano indicando si eres estudiante.

# %%
#Respuesta

# %% [markdown]
# ## 2. Variables en Python
# 
# ### Teoría
# Las variables son espacios de memoria donde almacenamos datos. En Python, no es necesario declarar el tipo de la variable, simplemente se asigna un valor con el símbolo `=`.
# 
# #### Reglas para nombrar variables:
# - Deben comenzar con una letra o un guion bajo.
# - No pueden comenzar con un número.
# - Solo pueden contener letras, números y guiones bajos.
# - Son sensibles a mayúsculas y minúsculas (`nombre` y `Nombre` son diferentes).
# 
# ### Ejemplo

# %%
# Declaración de variables
mi_nombre = "Carlos"
edad = 20

# Variables válidas
nombre_completo = "Ana Pérez"
_variable_secreta = 42 # convención para indicar que esa variable es protegida.

# Variables inválidas (descomentar para ver los errores)
# 2variable = 10  # Error: no puede comenzar con un número
# nombre completo = "Juan"  # Error: no puede contener espacios

# %% [markdown]
# ## 3. Operaciones Básicas de Entrada y Salida
# 
# ### Teoría
# Las operaciones de entrada y salida son fundamentales para interactuar con el usuario. En Python, utilizamos la función `input()` para capturar datos del usuario y `print()` para mostrar información en pantalla.
# 
# ### Ejemplos

# %%
# Operación de salida
print("¡Hola, mundo!")

# Operación de entrada + Saalida con format


# %% [markdown]
# En otros lenguajes, como *Java*, el proceso es similar pero con algunas diferencias en la sintaxis:
# 
# ```Java
# // Ejemplo en Java
# import java.util.Scanner;
# 
# public class EntradaSalida {
#     public static void main(String[] args) {
#         Scanner input = new Scanner(System.in);
#         System.out.print("¿Cómo te llamas? ");
#         String nombre = input.nextLine();
#         System.out.println("Hola, " + nombre + "!");
#     }
# }
# 
# ```

# %% [markdown]
# ## 4. Operadores Básicos en Python
# 
# ### Teoría
# Los operadores en Python nos permiten realizar diversas operaciones con variables y datos. Los más comunes son:
# 
# - **Operadores matemáticos**: `+`, `-`, `*`, `/`, `//` (división entera), `%` (módulo)
# - **Operadores de asignación**: `=`, `+=`, `-=`, `*=`, `/=`
# - **Operadores de comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
# - **Operadores lógicos**: `and`, `or`, `not`
# 
# ### Tabla de Operadores Matemáticos
# 
# | Operador | Descripción           | Ejemplo           |
# |----------|-----------------------|-------------------|
# | `+`      | Suma                  | `5 + 3 = 8`       |
# | `-`      | Resta                 | `5 - 2 = 3`       |
# | `*`      | Multiplicación         | `5 * 2 = 10`      |
# | `/`      | División              | `10 / 2 = 5.0`    |
# | `//`     | División entera        | `10 // 3 = 3`     |
# | `%`      | Módulo (resto)         | `10 % 3 = 1`      |
# 
# ### Ejemplos

# %% [markdown]
# #### Problema 1: Operadores Matemáticos y Comparación en Python
# 
# Tienes dos variables `a = 10` y `b = 5`. Realiza las siguientes operaciones matemáticas:

# %%
# Asignacón de variables


# Suma y resta


# %% [markdown]
# #### Problema 2: Comparación de Números
# Usa los siguientes operadores de comparación para verificar la relación entre a y b. ¿Qué resultado esperas?

# %%
# Operadores de comparación


# ¿Es a igual a b?

# ¿Es a mayor que b?

# ¿Es a menor que b?

# %% [markdown]
# ### Problema 3: Operadores Lógicos
# Usa operadores lógicos para combinar condiciones. Resuelve el siguiente problema: ¿Es a mayor que 0 y b menor que 10? ¿Qué pasa si a = -10?

# %%
# Operadores lógicos
contrasena = True
correo = True

# ¿Ambas condiciones son verdaderas?

# ¿Al menos una de las condiciones es verdadera?

# ¿Es falso que a sea mayor que b?


# %% [markdown]
# ### Problema 4: Divisiones y Módulo
# Prueba las operaciones de división entera y módulo para ver cómo Python maneja los restos de las divisiones.

# %%
# División entera y módulo
#Respuesta1
numero1 = int(input("Ingrese el primer numero: "))
numero2 = bool(input("Ingrese el segundo numero: "))
print(numero1, numero2)
#Respuesta2
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 % numero2)
#Respuesta3
print(numero1 + numero2>20) and (numero1 + numero2<5)


# %% [markdown]
# ### Ejercicio Final:
# 
# Combina operadores matemáticos, de comparación y lógicos. Escribe un programa que pida al usuario dos números y realice las siguientes tareas:
# 
# 1. Verifique si el primer número es mayor que el segundo.
# 2. Calcule la suma, resta, división y módulo de ambos.
# 3. Determine si la suma de ambos números es mayor que 20 **y** si alguno de los dos es menor que 5.

# %%
#Respuesta

# %% [markdown]
# # Estructuras de datos elementales
# 
# # Listas
# 
# Las listas son uno de los tipos de datos más importantes y versátiles en Python. Son colecciones ordenadas y mutables que pueden almacenar cualquier tipo de dato, desde números y cadenas de texto hasta objetos complejos.
# 
# **Creación de listas:**
# 
# Las listas se pueden crear de varias maneras:
# 
# - **Usando corchetes (**[]**) y separando los elementos por comas:**

# %%
#Creando mi primera lista

# %%
#TRABAJEMO CON LISTAS
#          0 1 2 3 4
miLista = [1,2,3,4,5]
cantidad = len(miLista)
print(f" Tamaño de la lista {cantidad}")
# Para acceder a sus elementos, se utiliza el [Índice] los índices comienzan en 0

# %%
#Usando la función print() y la función * para desempaquetar los elementos de la lista como argumentos")

# %%
#Usando un bucle "for" para imprimir todos los elementos de la lista.  

# %%
# Imprimir la cantidad elementos

# %% [markdown]
# ## Métodos básicos y útiles en Listas 
# 
# ### Agregar elementos a una lista en Python
# Existen dos métodos principales para agregar elementos a una lista en Python:
# 
# 1. append()
# 2. insert()

# %%
#append(): Este método agrega un elemento al final de la lista
correos = ["Outlook","Hotmail","Gmail"]
correos.append('Yahoo')
print(correos)

# %%
#insert(): Este método agrega un elemento en una posición específica
correos.insert(1," Proton Mail")
print(correos)

# %% [markdown]
# ### Agregar múltiples elementos a una lista

# %%
# extend() Agrega los elementos de una lista iterable al final de la lista original
paquete = ['Word','Excel','Power Point']
adicional = ['Acces','Visio','Skype']
print(paquete)
paquete.extend(adicional)
print(paquete)
paquete = ['Word','Excel','Power Point']
adicional = ['Acces','Visio','Skype']
paquete_pro = paquete + adicional
print(paquete_pro)


# %%
#Repitir listas utilizando operador de multiplicación (*)
Lista1 = [1,2,3]
lista_duplicada = Lista1*2
print(lista_duplicada)
print(2*lista_duplicada)

# %% [markdown]
# ## Métodos para eliminar elementos de una lista en Python

# %%
#remove(): Este método elimina el primer elemento de la lista que coincida
print(correos)
correos.remove("Proton Mail")
print(correos)
correos.remove(correos[1])

# %%
#pop(): Este método elimina y devuelve el elemento en una posición específica de la lista por medio del índice.
correos.insert(1,"Proton Mail")
print(correos)
eliminado = correos.pop(2)
print (correos)
print ("El elemento eliminado es", eliminado)
correos.pop(1)
print(correos)

# %%
#del Elimina elemento por índice
correos = ['Gmail','Hormail','outlook']
print(correos)
del(correos [2])
print(correos)
len(correos)


# %%
#clear(): este métolo eliminar los elementos de una lista
print(correos)
correos.clear()
print(correos) 


# %% [markdown]
# # Tuplas
# 
# Las **tuplas** son una de las estructuras de datos básicas en muchos lenguajes de programación, incluyendo Python. Son colecciones ordenadas y **inmutables** de elementos. Esto significa que una vez que se crea una tupla, no es posible modificar sus elementos (no se pueden añadir, eliminar, o cambiar valores).
# 
# ## Características de las Tuplas
# 
# - **Ordenadas**: Los elementos en una tupla tienen un orden definido.
# - **Inmutables**: Una vez creada, la tupla no puede cambiar. Los elementos no pueden ser modificados, añadidos, o eliminados.
# - **Indexables**: Puedes acceder a los elementos de la tupla por su índice, siendo `0` el índice del primer elemento.
# - **Permiten duplicados**: Las tuplas pueden tener elementos duplicados.
# 
# ## Creación de Tuplas
# 
# Para crear una tupla en Python, simplemente coloca los elementos dentro de paréntesis `()` y sepáralos con comas.

# %%
#Acceder a elementos de una tupla:
tupla = (1,2,3,'a','b','c')
print(tupla[1]) #2
print(tupla[3]) #2, "a"
for elemento in tupla:
    print(elemento)


# %%
#Utilizar una tupla en un ciclo for:
tupla_persona = ('Juan', 'Pérez', '25')
nombre,apellido,edad = tupla_persona
print( tupla_persona[1])
print(apellido)



# %%
#Asignar valores de una tupla a variables:
nueva_tupla =tupla + tupla_persona
print(nueva_tupla)

# %%
#Concatenar dos tuplas:
tupla_persona = ('Juan', 'Pérez', '25')
if 'juan' in tupla_persona:
    print('Bienvenido Juan')

# %%
#Comprobar si un elemento está en una tupla: Se puede usar el operador in para verificar si un elemento está presente en una tupla.


# %% [markdown]
# ### Funciones útiles:
# 
# - **len(tupla)**: Devuelve la longitud de la tupla.
# - **max(tupla)**: Devuelve el elemento máximo de la tupla.
# - **min(tupla)**: Devuelve el elemento mínimo de la tupla.
# 
# ### Cuándo usar tuplas:
# 
# Las tuplas son una buena opción para almacenar datos que no van a cambiar, como:
# 
# - Coordenadas en un mapa.
# - Fechas y horas.
# - Pares clave-valor en un diccionario.

# %%
tupla = (1,2,3,2,'a','b','c')
print(tupla)
print(tupla[0])
print(tupla[3])

# %%
posicion = tupla.index('b')
print("Posición: ", posicion)

# %%
numDos = tupla.count(2)
print("Cantida de repeticiones de dos: ", numDos)

# %%
#Utilizar una tupla en un ciclo for:
#Utilizar una tupla en un ciclo for:
for elemento in tupla:
    print(elemento)

# %%
#Asignar valores de una tupla a variables:
tupla = ("Luis", "Ferreto", 32)
Nombre,Apellido,edad = tupla
print(Nombre)
print(Apellido)
print(edad)

# %%
#Concatenar dos tuplas
Tupla1 = (1,2,3)
Tupla2 = (4,5,6)
Tupla3 = Tupla1 + Tupla2
print(Tupla3)

# %% [markdown]
# 
# ## **Creación de diccionarios:**
# Los diccionarios son colecciones no ordenadas que almacenan pares
# clave-valor en Python. Son una herramienta poderosa para almacenar y
# acceder a datos de una manera eficiente.
# 
# Los diccionarios se pueden crear de varias maneras:
# 
# -   **Usando llaves **{}** con pares clave-valor separados por dos
#     puntos:**
# 
# ```Python

# %%
#Crear un diccionario
estudiante = {
    'nombre' : 'Marta',
    'apellido' : 'Campos',
    'edad': 25,
    'nota': 88.40
}
print(estudiante['nombre']) # Imprime : Marta
print(type(estudiante['nombre']))


#Modificar valor en un diccionario
estudiante['nota'] = 98.40
print(estudiante['nota'])

# %%
#Agregar nuevos pares clave-valor a un diccionario
estudiante ['altura'] = 1.70
print(estudiante)

# %%
#Recorriendo Claves y valores en For
for clave,valor in estudiante.items():
    print(f'Clave: {clave} , valor : {valor}')
for elementos in estudiante:
    print(elementos, ":", estudiante[elementos])   
    

# %%
#Eliminar elementos del diccionario
del estudiante['altura']
print(estudiante)
    

# %%
#Comprobar si una clave existe en el diccionario
estudiante.clear()
del estudiante
estudiante.pop[1]


# %%
#Zip(). Esta función toma dos o más listas y devuelve un 
# objeto iterable que contiene tuplas con los elementos
# correspondientes de cada lista.

print('nombre' in estudiante)
print('altura' in estudiante)



