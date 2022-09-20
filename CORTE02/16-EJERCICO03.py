## 16-EJERCICO 03 RECURSIÓN
'''
Los ejercicios son de caracter obligatorio, sin embargo no se les asignará una calificación, el objetivo de estos
es que ustedes practiquen y mejoren sus habilidades.
estos los deben subir de manera individual en su cuenta de Git
'''
'''
se les darán multiples funciones, así como la documentación correspondiente
 deben completar las tareas marcadas como TODO
'''
## DEMOSTRACIONES MATEMATICAS
# ejercicios tomados de: https://elvex.ugr.es/decsai/java/pdf/7D-Ejercicios.pdf

#TODO: Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n

#TODO: Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?
#Solucion:
def f_contarconejos(parejas):
    if parejas<2:#En caso de que el numero de parejas sea menor que 2.
        return parejas #El numero de parejas se almacena y retorna.
    parejas_tot= f_contarconejos(parejas-1)+f_contarconejos(parejas-2)#Las parejas totales son la suma de las 2 anterirores.
    return parejas_tot #Impimimos valor de parejas totales.
print(f_contarconejos(13))#Para un año el resultado sera:

## Ejercicio objetos.
# TODO: 1. Cree un archivo, Taller donde llevará acabo el codigo principal
#       crear una lista de vehiculos que se encuentran en el taller en ese momento que tienen asociados: fecha de entrega, costo, modelo, año y dueño
#       crear una caja donde se almacena el dinero y se lleva registro de los movimientos
#       crear una lista de empleados que tienen asociado un nombre, cargo, salario, vehiculo y documento
#       Crear una lista de clientes que tienen asociado un nombre, vehiculo y documento

# TODO: 2 Ejecute sobre so codigo principal:
#       ingresar un vehiculo nuevo al taller (validar cupo)
#       Sacar un vehiculo del taller (se debe generar un pago por parte del cliente)
#       PAgar a los empleados (se debe hacer una reducción en el dinero de la caja)
#       Contrarar a una persona nueva
#       Despedir a una persona
#       Encontrar un vehiculo a partir de su dueño y determinar si está en el taller
# TODO: 3 Todas las funciones que implemente deben estar en un script distinto al principal y donde se definen sus clases
#       NOTA - (la UNICA exepción son las funciones que definen dentro de sus clases.)
class Vehiculo():

    fechaEntrega = "" 
    costo = 0.0 
    modelo = "" 
    anio = 0 
    duenio = None 

    def _init_(self, fechaEntrega, costo, modelo, anio, duenio):
        self.fechaEntrega = fechaEntrega 
        self.costo = costo 
        self.modelo = modelo 
        self.anio = anio 
        self.duenio = duenio 
        
    def informacion(self, fechaEntrega, costo, modelo, anio, duenio):
     '''
     A continuacion se utiliza el print para imprimir lo que se muestra en la linea siguiente en este caso cada uno de los parametros
     en los que se usa el self para identificar que se establando de los parametros de la misma clase vehiculo 
     '''
        print
        self.fechaEntrega
        print
        self.costo
        print
        self.modelo
        print
        self.anio
        print
        self.duenio
mustang = vehiculo()
mustang.fechaEntrega = '13/07/2023'
mustang.costo= '200000000'
mustang.modelo = 'Match 1'
mustang.anio = '1965'
mustang.duenio = 'Albert'
mustang.print_information(mustang.d_delivery,mustang.cost,mustang.model,mustang.year,mustang.owner) 

class Caja(): 
    dineroTotal = 0.0 
    movimientos = [] 
    def _init_(self, dineroTotal): 
        self.dineroTotal = dineroTotal 

    def pagarEmpleados(self, empleados): 
        totalAPagar = 0.0
        i = 0
        while i < len(empleados):
            totalAPagar += empleados[i].salario 
            i+=1 
        if(self.dineroTotal >= totalAPagar):  
            self.dineroTotal -= totalAPagar 
            return True
        return False

    def ingresarDinero(self, dineroIngresado):
        self.dineroTotal += dineroIngresado 
  class GestionVehiculos():
    vehiculos = [] 

    def _init_(self, vehiculos):
        self.vehiculos = vehiculos

    def ingresarVehiculo(self, vehiculo, cantidadEmpleados):
        if(len(self.vehiculos)<cantidadEmpleados): 
            self.vehiculos.append(vehiculo)
            return True
        return False

    def sacarVehiculo(self, vehiculo):
        if(len(self.vehiculos)>0):
            if(vehiculo in self.vehiculos):
                self.vehiculos.remove(vehiculo)
                return True
        return False
 class GestionEmpleado():
    empleados = []

    def _init_(self, empleados):
        self.empleados = empleados

    def buscarEmpleado(self, documento):
        print("falta")

    def contratarEmpleado(self, empleado):
        self.empleados.append(empleado)
        return True


    def despedirEmpleado(self, empleado):
        if(len(self.empleados) > 0):
            self.empleados.remove(empleado)
            return True
        return False
       
from Vehiculo import Vehiculo


class Empleado():
    nombre = ""
    cargo = ""
    salario = 0.0
    vehiculo = None
    documento = 0

    def _init_(self, nombre, cargo, salario, vehiculo, documento):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.vehiculo = vehiculo
        self.documento = documento
        
from Vehiculo import Vehiculo

class Cliente():
    nombre = ""
    documento = 0

    def _init_(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

