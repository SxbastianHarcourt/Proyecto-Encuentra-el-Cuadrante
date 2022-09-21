# Proyecto Módulo 2 : Encuentra el cuadrante.
# Víctor Sebastian Rosales Sánchez

print ("""Bienvenido al buscador de cuadrantes.
Por favor, sigue las indicaciones.

NOTA: No se puede ingresar el valor de cero [0]
""") # Se coloca un mensaje de bienvenida y se le indica al usuario las condiciones del programa.

coordenadas = [] # Se hace una lista vacía, a l cual se la agregarán las coordenadas correspondientes.

x = float (input ('Ingrese el valor del eje X: ')) # Variable para el eje x
y = float (input ('Ingrese el valor del eje Y: ')) # Variable para el eje y

if x > 0: # Condición: Si x es mayor a cero, es decir, si es positiva, entonces se añade a la lista 'coordendas'.
    coordenadas.append(x)
    if y > 0 : # Si 'y' es positiva, entonces se agrega su valor a la lista 'coordenadas'.
        coordenadas.append(y)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas) # Se imprime la lista de coordenadas, para que el usuario conozca los valores ingresados.
        print ("El punto se encuentra en el cuadrante I") # Se imprime en qué cuadrante se encuentra el punto indicado, según el signo de cada coordenada.
        exit ()
    elif y < 0 : # Si 'y' es negativa, entonces se agrega su valor a la lista 'coordenadas'.
        coordenadas.append(y)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas) # Se imprime la lista de coordenadas, para que el usuario conozca los valores ingresados.
        print ("El punto se encuentra en el cuadrante IV") # Se imprime en qué cuadrante se encuentra el punto indicado, según el signo de cada coordenada.
        exit()
    else :
        print ('ERROR: No se puede ingresar como coordenada en Y el valor de cero o los datos ingresados son incorrectos.')
        exit () # Si se ingresa un cero o caracteres alfabéticos, se indicará un mensaje de error.

elif x < 0: # Condición: Si x es menor a cero, es decir, si es positiva, entonces se añade a la lista 'coordendas'.
    coordenadas.append(x)
    if y > 0 : # Si 'y' es positiva, entonces se agrega su valor a la lista 'coordenadas'.
        coordenadas.append(y)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas) # Se imprime la lista de coordenadas, para que el usuario conozca los valores ingresados.
        print ("El punto se encuentra en el cuadrante II") # Se imprime en qué cuadrante se encuentra el punto indicado, según el signo de cada coordenada.
        exit ()
    elif y < 0 : # Si 'y' es negativa, entonces se agrega su valor a la lista 'coordenadas'.
        coordenadas.append(y)
        print ('Las coordenadas ingresadas son:')
        print (coordenadas) # Se imprime la lista de coordenadas, para que el usuario conozca los valores ingresados.
        print ("El punto se encuentra en el cuadrante III") # Se imprime en qué cuadrante se encuentra el punto indicado, según el signo de cada coordenada.
        exit()
    else :
        print ('ERROR: No se puede ingresar como coordenada en Y el valor de cero o los datos ingresados son incorrectos.')
        exit () # Si se ingresa un cero o caracteres alfabéticos, se indicará un mensaje de error.

else :
    print ('ERROR: No se puede ingresar como coordenada en X el valor de cero o los datos ingresados son incorrectos.')
    exit () # Si se ingresa un cero o caracteres alfabéticos, se indicará un mensaje de error.
