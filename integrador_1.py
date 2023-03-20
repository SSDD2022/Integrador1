''' 
  1. Escribir una función que calcule el máximo común divisor entre dos números.
     Maximo valor divisible por ambos
'''
def maximo_comun_divisor(num1, num2):
    tope = min(num1, num2)
    for i in range(tope,1,-1):
        if (num1%(i)) == 0 and (num2%(i) == 0):
            print (f'El máximo común divisor entre {num1} y {num2} es {i}')
            return
    print (f'No se encontró el máximo común divisor entre {num1} y {num2}')
'''
maximo_comun_divisor(10,5)
maximo_comun_divisor(32,28)  # 4
maximo_comun_divisor(90,60)
maximo_comun_divisor(7,17)
'''

'''
  2. Escribir una función que calcule el mínimo común múltiplo entre dos números
     Menor número divisible por ambos.
'''
def minimo_comun_multiplo(num1, num2):
    desde = max(num1, num2)
    tope = num1 * num2
    for i in range(desde,tope+1,desde):
        if (i%num1) == 0 and (i%num2) == 0:
            print (f"El mínimo común múltiplo entre {num1} y {num2} es {i}")
            return
    print (f"No se encontró el mínimo común múltiplo entre {num1} y {num2}")
'''
minimo_comun_multiplo(10,5)
minimo_comun_multiplo(9,6)
minimo_comun_multiplo(12,40)  # 120
minimo_comun_multiplo(7,17)
'''

'''
 3. Escribir un programa que reciba una cadena de caracteres
    y devuelva un diccionario con cada palabra que contiene y
    la cantidad de veces que aparece (frecuencia)
'''
'''
  Ejemplo de llamado:
  & C:/Users/Silvia/AppData/Local/Programs/Python/Python311/python.exe c:/Users/Silvia/Desktop/Django/Integrador1/integrador_1_main.py -p "Si puedes soñarlo, puedes conseguirlo" 
'''

'''
 4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada 
    palabra que contiene y la cantidad de veces que aparece (frecuencia). 
    Escribir otra función que reciba el diccionario generado con la función anterior y
    devuelva una tupla con la palabra más repetida y su frecuencia
'''
def armar_diccionario(cadena):
    resultado = {}
    lista = cadena.lower().split(' ')
    print ("Lista:",lista)
    for palabra in lista:
        resultado.update ({palabra : lista.count(palabra)})  # No repite ocurrencias
    return (resultado)
def armar_tupla(diccionario):
    maximo = max(diccionario.values())
    for key, value in diccionario.items():
        if value == maximo:
            return key, value
'''
cadena = "Si puedes soñarlo, puedes conseguirlo"
diccio = armar_diccionario(cadena)
print (f"Diccionario: {diccio}")
tupla = armar_tupla(diccio)
print (f"Tupla: {tupla}")
'''

'''
5. ValueError excepción por no poder convertir una cadena de texto en su valor numérico
   Escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
   iterando mientras el valor no sea correcto. 
   Intente resolver el ejercicio tanto de manera iterativa como recursiva. 
'''
def get_int():
    while True: 
        try:
            val = int (input('Ingrese un número: '))
        except ValueError:
            print ("Debe ser un número")
        else:
            break
    return (val)
'''
print (f'Número ingresado: {get_int()}')
'''

def get_int():
    try:
        val = int (input('Ingrese un número: '))
    except ValueError:
        val = get_int()
    return (val)
'''
print (f'Número ingresado: {get_int()}')
'''

'''
 6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
    Métodos: 
    - Un constructor, donde los datos pueden estar vacíos. 
    - Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. 
    - mostrar(): Muestra los datos de la persona. 
    - Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''
class Persona():
    def __init__(self,nombre=None,edad=None,DNI=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    # getters
    @property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        if self.__edad is None:
            return 0
        return self.__edad
    @property
    def DNI(self):
        return self.__DNI   

    # setter
    @nombre.setter
    def nombre(self, nombre):
        if not (nombre):
            print ("El nombre es obligatorio")
        else:
            self.__nombre = nombre
    @edad.setter
    def edad(self, edad):
        try:
            if int(edad) < 1 or int(edad) > 130:
                print (f'Edad {edad} inválida, debe estar entre 1 y 130')
            else:
                self.__edad = edad
        except ValueError:
            print ('La edad debe ser numérica')
    @DNI.setter
    def DNI(self, dni):
        try:
            if int(dni) < 0:
                print ('Numero de DNI inválido {dni}')
            else:
                self.__DNI = dni
        except ValueError:
            print ('El DNI sólo debe tener números')

    def mostrar(self):
        print (f'Persona llamada {self.nombre} con {self.edad} años y DNI {self.DNI}')
    def Es_mayor_de_edad(self):
        return (self.edad >= 18)

'''   
Persona1 = Persona()
Persona1.nombre = ''
Persona1.nombre = 'Juan'
Persona1.edad = 16
Persona1.DNI = 35600700
Persona1.mostrar()
if Persona1.Es_mayor_de_edad:
    print (f'{Persona1.nombre} es mayor de edad')
else:
    print (f'{Persona1.nombre} no es mayor de edad')

Persona2 = Persona('Pablo',43,25800400)
Persona2.mostrar()
if Persona2.Es_mayor_de_edad:
    print (f'{Persona2.nombre} es mayor de edad')
else:
    print (f'{Persona2.nombre} no es mayor de edad')
'''

'''
 7. Crea una clase llamada Cuenta que tendrá 
    - los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
      El titular será obligatorio y la cantidad es opcional. 
    - los siguientes métodos: 
        - Un constructor, donde los datos pueden estar vacíos. 
        - Los setters y getters para cada uno de los atributos. 
          El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
        - mostrar(): Muestra los datos de la cuenta. 
        - ingresar(cantidad): se ingresa una cantidad a la cuenta, 
          si la cantidad introducida es negativa, no se hará nada. 
        - retirar(cantidad): se retira una cantidad a la cuenta. 
          La cuenta puede estar en números rojos. 
'''
class Cuenta():
    def __init__(self,nombre,edad,dni,cantidad=None):
        try:
            if cantidad is None:
                self.__cantidad = 0
            else:
                self.__cantidad = float(cantidad)
        except ValueError:
            print ('Se espera un importe')
        self.__titular = Persona(nombre,edad,dni)

    # getters
    @property
    def cantidad(self):
        return self.__cantidad
    @property
    def nombre(self):
        return self.__titular.nombre
    @property
    def edad(self):
        return self.__titular.edad
    @property
    def DNI(self):
        return self.__titular.dni

    def mostrar(self):  # Da error usar el getter
        return (f'Titular {self.__titular.nombre} de {self.__titular.edad} años con DNI {self.__titular.DNI} y saldo {self.cantidad}')
 
    def Es_mayor_de_edad(self):
        return self.__titular.Es_mayor_de_edad()

    # setters 
    def ingresar(self, valor):
        try:
            if float(valor) > 0:
                self.__cantidad += valor
            else:
                print('Se espera un importe positivo')
        except ValueError:
            print ('Se espera un importe')

    def retirar(self, valor):
        try:
            if float(valor) > 0:
                self.__cantidad -= valor
            else:
                print('Se espera un importe positivo')
        except ValueError:
            print ('Se espera un importe')
'''
cta0 = Cuenta('Agos',25,10000000,'Ahora')
cta1 = Cuenta('Maria',50,18400300)
print (cta1.mostrar())
cta1.ingresar(50)
cta1.ingresar(-1000)
cta1.retirar(40)
print ('Valor actual:',cta1.cantidad)
print (cta1.mostrar())
cta1.retirar(56.80)
print (cta1.mostrar())
print ("Edad del titular",cta1.edad)
'''
'''
 8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
    CuantaJoven que deriva de la clase creada en el punto 7. 
    Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación
    que estará expresada en tanto por ciento. 
    Crear los siguientes métodos para la clase: 
    - Un constructor. 
    - Los setters y getters para el nuevo atributo. 
    - En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
      por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
      mayor de edad pero menor de 25 años y falso en caso contrario. 
    - Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
    - El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta. 
'''
class DatoInvalido(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class CuentaJoven(Cuenta):
    def __init__(self,nombre,edad,DNI,cantidad,bonificacion):
        try:
            if float(bonificacion) >= 0 and float(bonificacion) <= 100:
                self.__bonificacion = bonificacion
            else:
                raise DatoInvalido('La bonificación debe ser un %')
        except ValueError:
            print (f"Bonificación {bonificacion} es inválida, debe ser un %")
        super().__init__(nombre,edad,DNI,cantidad)

    # getters
    @property
    def bonificacion(self):
        return self.__bonificacion

    def mostrar(self):
        return(f'Cuenta Joven con una bonificación de: {self.bonificacion}')

    # setters
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        try:
            if float(bonificacion) >= 0 and float(bonificacion) <= 100:
                self.__bonificacion = bonificacion
            else:
                raise DatoInvalido('La bonificación debe ser un %')
        except ValueError:
            print (f"Bonificación {bonificacion} es inválida, debe ser un %")

    def es_titular_valido(self):
        return super().Es_mayor_de_edad and self.edad < 25 

    def retirar(self,valor):
        if self.es_titular_valido():
            super().retirar(valor)

'''
print ('------------------------------')
ctaJoven1 = CuentaJoven ('Luis',40,2500600,1000.50,9.10)

print('Cantidad: ',ctaJoven1.cantidad)
print(ctaJoven1.mostrar()) 
ctaJoven1.bonificacion = 25.30
print(ctaJoven1.mostrar())
ctaJoven1.ingresar(200)
ctaJoven1.retirar(300)  # No lo hace
print(ctaJoven1.cantidad)
print (ctaJoven1.es_titular_valido())
ctaJoven1.retirar(400)
print(ctaJoven1.cantidad)

ctaJoven2 = CuentaJoven ('Laura',20,34000200,10000,25.2)
print(ctaJoven2.mostrar())
ctaJoven2.retirar(5000)
print(ctaJoven2.cantidad)
'''