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
Punto N1:
l_paises = ['Colombia','Mexico','Turquia','Polonia','serbia','dinamarca','holanda','Alemania']#Creamos la lista con los paises.
l_paises1=""#Creamos una lista donde se añadran los paises en orden y con su respectiva mayuscula.
for i in range(0,8,1):#Iniciamos un bucle para que recorra la lista.
    l_paises1+=l_paises[i].capitalize()#Creamos funcion para las mayusculas en cada elemento de la lista.
    l_paises1+=", "#Creamos funcion para que haya una coma y un espacio.
archi1=open("datos.txt","w")#Definimos el archivo txt y le asignamos un nombre.
with open('datos.txt', 'w') as temp_file:#Generamos el archivo txt y empezamos a escribir en el.
    for item in l_paises1:#Iniciamos ciclo para la lista.
        temp_file.write("%s" % item)#Escrbimos lo guardado en la lista en el txt.
file = open('datos.txt', 'r')#Abrimos el erchivo txt.
print(file.read())#Imprimimos la funcion para comprobar.

Punto N2:
str_archivo = open("datos.txt")#Abrimos el acrhivo txt.
print(str_archivo.read())#Imprimimos en la consola el archivo.

Punto N3:
def f_calBin (s_num): #Iniciamos la funcion con el numero que se va a calcular (parametro).
    s_num=s_num+0.0 #
    print(s_num) #Imprimimos el numero.
    s_residuo=0 #Iniciamos la variable residuo.
    lista=[]
    s_bin = []#Creamos dos listas vacias que llevaran las partes enteras del numero y otra el residuo.
    str_num=str(s_num)
    split_num=str_num.split(sep=".")
    s1_num=int(split_num[0])
    s2_num=int(split_num[1])#Iniciamos la  variables.

    while s1_num!=0: #Iniciamos ciclo para s1.
        s_residuo =s1_num % 2#Decimos que para residuo sera el resultado de la operacion.
        s1_num=s1_num//2
        lista.append(s_residuo)#Añadimos a la lista el residuo.
    k = len(lista) - 1
    while (k >= 0):#Iniciamos ciclo en el caso de k.
        s_bin.append(lista[k])#Añadimos a la lista s_bin k.
        k = k - 1
    s_bin.append(".")#Añadimos un punto a la lista.

    for i in range(4): #Iniciamos ciclo que recorra la lista en el rango 4.
        notacion=len(str(s2_num))
        s2_num=s2_num*(10**(-notacion))
        s2_num=s2_num*2
        s2_num=str(s2_num)
        splits2_num=s2_num.split(sep=".")
        s_bin.append(int(splits2_num[0]))
        s2_num=int(splits2_num[1])
        if s2_num==0:
            break
    s_bin="".join([str(_) for _ in s_bin])
    return (f'El numero en decimal es: {s_bin}')#Retornamos la lista con el deecimal.
print(f_calBin(45))#Imprimimos.
Punto 4:
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
