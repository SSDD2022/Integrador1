import argparse
import sys


def armar_diccionario(cadena):
    resultado = {}
    lista = cadena.lower().split(' ')
    print ("Lista:",lista)
    for palabra in lista:
        resultado.update ({palabra : lista.count(palabra)})  # No repite ocurrencias
    return (resultado)

def main(cliParams=None):
    cadena = get_params(cliParams)
    print (f"Cadena recibida como parámetro: {cadena}")
    diccionario = armar_diccionario(cadena)
    print (f"Diccionario: {diccionario}")
    return diccionario

'''
  Parsea los parametros, o indica cuales se deben informar
'''
def get_params(cliParams=None):
  parser = argparse.ArgumentParser()
  parser.add_argument("-p", "--parametro-cadena", action="store", required=True)

  if not cliParams:
    args = parser.parse_args()
  else:
    args = parser.parse_args(cliParams.split())

#  return [args.parametro_cadena]   # Devuelve una lista
  return args.parametro_cadena      # Devuelve una cadena

# Solo se ejecuta main si se invoca desde el entorno
if __name__ == "__main__":
  main()

'''
  Ejemplo de llamado:
  & C:/Users/Silvia/AppData/Local/Programs/Python/Python311/python.exe c:/Users/Silvia/Desktop/Django/integrador_clase7_main.py -p "Si puedes soñarlo, puedes conseguirlo" 
'''