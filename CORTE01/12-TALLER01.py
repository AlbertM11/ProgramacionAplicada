## 12-TALLER 01
'''
El presente taller tiene como objetivo evaluar las habilidades adquiridas hasta el momento a lo largo del curso,
así como repasar los conceptos e introducir nuevas herramientas.
'''
# Recordatorio, el archivo lo deben subir a su repositorio en la fecha indicada.
## 1. Persistencia (1.0)
l_paises = ['Colombia','Mexico','Turquía','Polonia','serbia','dinamarca','holada','Alemania']
#TODO: escriba un programa que le permina escribir de manera automatica los nombres de estos paises en un archivo txt
#NOTA: todos los nombres deben tener una mayuscula al comienzo
#       el archivo se ecuentra en formato csv
## 2. Lectura de archivos (1.0)
#TODO: escriba un programa que le permita leer e imprimir el archivo generado anteriormente

## 3. números binario (1.5)
def f_calBin (s_num):
    '''
    Calculadora que permite encontrar la representación en binario de un número entero o decimal que ingresa por parametro
    :param s_num: número que se desea convertir a binario int o float
    :return: valor número en binario
    '''
    #TODO: escribir la sección del codigo para las conversiones
    #NOTA: puede hacer uso de tantas funciones como necesite (diseñadas por el estudiante)
    s_bin = 0 #deben asignal el valor binario en esta variable
    return s_bin

#Test

assert f_calBin (1) == 1
assert f_calBin (4) == 100
assert f_calBin (10) == 1010
assert f_calBin (1.25) == 1.01

## 4. Valores estadisticos (1.5)
import numpy as np
def f_stat (l_valores):
    '''
    función que toma una lista de valores y retorna el promedio, la mediana y la desviación estandar
    :param l_valores: lista con los valores a utilizar
    :return:
    '''
    s_mean, s_median, s_STD = 0,0,0
    #TODO: realizar las modificaciones necesarias a partir de esta sección
    return s_mean,s_median,s_STD

## 5. BONO (0.5)
#TODO: realizar la verificación del punto aterior haciendo uso de la función assert (pytest)
import numpy as np #Importamos la libreria numpy.
l_valores = [9,2, 9, 4, 5, 1, 8, 7, 8, 8, 9, 10,3]#Creamos una lista con los valores.
def f_stat(l_valores):#Creamos una funcion para la media en el range de la lista.
    s_mean, s_median,str_ordn,int_contadora,int_divisor,str_ordn = 0, 0, 0, 0,len(l_valores),np.sort(l_valores)#Definimos las variables.
    s_mean=sum(l_valores)/int_divisor
    half=int_divisor//2#Declaramos divisor.
    if not int_divisor%2:#Iniciamos condicion.
        s_median=(l_valores[half-1]+l_valores[half])/2#Generamos el calculo en caso de que se cumpla la condicion.
    else:#De lo contrario.
        s_median=l_valores[half]#Generamos solucion en caso que no se cumpla.
    def mode(l_valores):#Creamos funcion para moda en el range de la lista.
      frequency = {}#Creamos diccionario para guardar las variables.
      for value in l_valores:#Iniciamos ciclo para value en el range de la lista.
          frequency[value] = frequency.get(value, 0) + 1#Iniciamos la funcion frequency para value.
      most_frequent = max(frequency.values())
      s_moda = [key for key, value in frequency.items()#Inicicamos ciclo para moda.
                        if value == most_frequent]#Creamos condicion para el valor de moda
      return s_moda #Retornamos la funcion.
    return (f"La media es:{s_mean}, y la mediana es: {s_median}, y la moda es: {mode(l_valores)}")#Retornamos la media de cada uno.
print(f_stat(l_valores))#Imprimimos la funcion y la lista.

En compañia con:
    Juan David Panadero.
    Maria Alejandra Leyton.
