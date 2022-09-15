#15-RECURSIÓN
'''
en este segmetno se mostrarán los algoritmos recursivos así como los explorar algunas de las aplicaciones de estas.
un algoritmo recursivo es aquel que se utiliza a sí mismo para cumplir una función.
normalmente estos algoritmos tienen a ser poco eficientes y requieren una gran cantidad de recursos, sin embargo,
dependiendo de la aplicación y la forma en que se manejen los datos pueden ser más eficientes que los algoritmos
vistos hasta el momento
'''
#Nota:todos los algoritmos recursivos se pueden escribir como ciclos y todos los algoritmos cicilos se pueden escribir
#     de manera recursiva
## contar hasta 10 haciendo uso de recursión

def f_contar(s_num): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema
    if s_num < 10: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        s_num+=1
        return f_contar(s_num) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final

print(f_contar(1))

# TODO: modificar esta función para que imprima todos los valores de manera ordenada:
def f_contar(s_num): #Iniciamos la funcion con su parametro correspondienete parametro para la correcta ejecucion.
    if s_num < 10: #En caso del numero ser menor que 10, sumar 1 y volver a ejecutar el programa.
        print(s_num, end = " ") #Imprimimos el numero que va en secuencia antes de la suma hasta cumplir con la condicion.
        s_num+=1
        return f_contar(s_num) #Al ejecutar la funcion ingresa con s_num + 1 como parametro por lo que incrementa.
    else:
        return s_num #Al cumplirse la funcion retorna el valor final.
print(f_contar(1))
# TODO: modificar la función para que reciba dos parametros, el número inicial y el objetivo:
def f_contar(s_num,s_objeto): #Iniciamos la funcion, con 2 parametros para que ejecute correctamente.
    if s_num < s_objeto: #Iniciamos condicion en caso de que el numero actual dado por el parametro es menor que el numero dado por el otro parametro, inicia el recorrido.
        print(s_num, end = " ") #Imprimimos el numero que va en secuencia antes de la suma hasta cumplir con la condicion.
        s_num+=1
        return f_contar(s_num,s_objeto) #Al ejecutar la funcion ingresa con s_num + 1 como parametro por lo que incrementa.
    else:
        return s_num #Al cumplirse la funcion retorna el valor final.
print(f_contar(1,12))
# TODO: modificar la función para que reciba 3 parametros el número inicial, el objetivo y los pasos entre números:
def f_contar(s_num,s_objeto,s_pasos): #Iniciamos la funcion, con 2 parametros para que ejecute correctamente.
    if s_num < s_objeto: #Iniciamos condicion en caso de que el numero actual dado por el parametro es menor que el numero dado por el otro parametro, inicia el recorrido.
        print(s_num, end = " ")#Imprimimos el numero que va en secuencia antes de la suma hasta cumplir con la condicion.
        s_num+=s_pasos  #Se utiliza el parametro inicial par iniciar el recorrido y se pide que la suma sea igual a la de los pasos.
        return f_contar(s_num,s_objeto,s_pasos) #Al ejecutar la funcion ingresa con s_num + 1 como parametro por lo que incrementa.
    else:
        return s_num #Al cumplirse la funcion retorna el valor final.
print(f_contar(1,12,2))


## Torre de Hanoi
'''
existen problemas que son por naturaleza recursivos, un ejemplo de estos es la torre de hanoi 
https://www.youtube.com/watch?v=vrXue8Lq1Ow&ab_channel=EdukativeS.L.-Rob%C3%B3ticaEducativaeningl%C3%A9s
https://www.geogebra.org/m/NqyWJVra
'''
# TODO: Implementar una solución recursiva a la torre de hanoi:
def Torre(ficha,A1,B2,C3):
    if ficha ==1: #Establecemos la sumatoria de una ficha a otra.
        print("la ficha se movera a ",A1,B2) #Imprimimos la ubicacion de la ficha A1 a B2.
        return #Retornamos.
    Torre(ficha - 1,A1,B2,C3) #En esta funcion lo que haremos sera que a la ficha colocada le contaremos como le restamos la ubicacion de una de estas.
    print("la ficha ",ficha,"se movera ",A1 ,"a",C3) #Imprimiremos como se movera la ficha.
    Torre(ficha - 1,C3,B2,A1)#En esta funcion lo que haremos seraque a la ficha puesta le contaremos como le restamos la ubicacion pero teniendo en cuenta como esta estara al reves.
Torre(3,"A1","B2","C3") #En esta funcion ubicaremos el numero de fichas a jugar y la ubicacion a las cuales las fichas se moveran en las que estan definidas como A1,B2,C3.

## Solución a la torre de Hanoi
#Algoritmo tomado de: https://www.delftstack.com/es/howto/python/tower-of-hanoi-python/
def ToH(n, A, B, C):
    if n == 1:
        print("Disk 1 from", A, "to", B)
        return
    ToH(n - 1, A, C, B)
    print("Disk", n, "from", A, "to", B)
    ToH(n - 1, C, B, A)


ToH(3, 'A', 'B', 'C')
