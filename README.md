# Proyecto Módulo 2: Encuentra el Cuadrante
**Creador:** Víctor Sebastian Rosales Sánchez

## ¿Qué se requiere? 💻
* Contar con una computadora/laptop y conexión a internet.
* Tener instalada la última versión de Python.
* Emplear Visual Studio Code como editor de texto.
* Tener descargado Git y vincular nuestro editor de texto a éste.

## Descripción del Proyecto 🤓
El objetivo del programa es indicar en qué cuadrante del sistema Cartesiano se encuentra un punto con coordenas específicas (ingresadas por el usuario), en donde:

* El **eje X** se encuentra como línea horizontal.
* El **eje Y** se encuentra como línea vertical.

Primero, al usuario se le da la bienvenida al programa y se le indican las condiciones para poder ejecutarlo.
Posteriormente, se indica una lista vacía, denominada 'coordenadas [ ]' , en la cual se van a anexar las coordenadas ingresadas por el usuario, para posteriormente imprimirlas.

Una vez realizada la lista, se le solicita al usuario que ingrese su coordenada en el 'eje x' a partir de una variable denominada "x" que emplee la función 'input( )'. Es importante que esta esté casteada para tener una variable de tipo 'float ( )', ya que los números ingresados deben ser tanto positivos como negativos, así como poder incluir números con decimales.

Una vez indicada las variable "x", se coloca la condición de que si "x" es positiva (mayor a cero), se sigan las siguientes condiciones:
* "x" se añada a la lista 'coordenadas [ ]' sí o sí.
* Se solicite al usuario que ingrese el valor de la coordenada "y", ya que si el valor de "x" es incorrecto el programa se dentendrá y se le solicitará al usuario ingresar un valor válido para la variable "x".
* Si "y" es mayor a cero, esta se añada a la lista 'coordenadas [ ]' , y se imprima el mensaje que el punto con las coordenadas ingresadas se encuentra en el **cuadrante I** [+, +].
* Si "y" es menor a cero, esta se añada a la lista 'coordenadas [ ]', y se imprima el mensaje que el punto con las coordenadas ingresadas se encuentra en el **cuadrante IV** [+, -].
* Si "y" es igual a cero, se imprima un mensaje que especifique que el valor de cero no es aceptado por el programa.

Sin embargo, también es necesario indicar la condición de que si "x" es negativa (menor a cero), se sigan las condiciones:
* "x" se añada a la lista 'coordenadas [ ]' sí o sí.
* Se solicite al usuario que ingrese el valor de la coordenada "y", ya que si el valor de "x" es incorrecto el programa se dentendrá y se le solicitará al usuario ingresar un valor válido para la variable "x".
* Si "y" es mayor a cero, esta se añada a la lista 'coordenadas [ ]' , y se imprima el mensaje que el punto con las coordenadas ingresadas se encuentra en el **cuadrante II** [-, +].
* Si "y" es menor a cero, esta se añada a la lista 'coordenadas [ ]', y se imprima el mensaje que el punto con las coordenadas ingresadas se encuentra en el **cuadrante III** [-, -].
* Si "y" es igual a cero, se imprima un mensaje que especifique que el valor de cero no es aceptado por el programa.

No obstante, es posible que el valor ingresado en "x" sea cero. Si este es el caso, se tiene la condición de imprimir un mensaje que especifique que el valor de cero no es aceptado por el programa.

Si cualquiera de estas condiciones para "x" no se cumple, se imprime un mensaje que indique que los valores ingresados no son válidos y que se debe de seguir las condiciones del programa. 

## ¿Qué me ha dejado el Bootcamp? 💬
El BootCamp me ha permitido comprender cómo funcionan los condicionales y ciclos, así como comprender cómo realizar la correcta asignación de variables, de forma que el programa tenga un orden y sintaxis correctas. Así mismo me ha permitido comprender cómo es que funcionan y se emplean las diferentes colecciones.


