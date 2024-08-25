#Fecha: 06/05/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

#Importando las librerias
from random import randint
import msvcrt
import platform
import os
from colorama import Fore,init, just_fix_windows_console

init()
just_fix_windows_console()

#Definiendo las listas
lista = []
pares = []
impares = []


def ingreso(): #Definiendo la función de ingreso
    print(Fore.GREEN + "")
    print("---------------------------------------------------------------")
    print("|                                                             |")
    print("|                                                             |")
    print("|                                                             |")
    print("|        BIENVENIDO AL GENERADOR DE LISTA ALEATORIA           |")
    print("|          PARA INGRESAR PRESIONE CUALQUIER TECLA             |")
    print("|                                                             |")
    print("|                                                             |")
    print("|                                                             |")
    print("---------------------------------------------------------------")
    msvcrt.getch()
    platform.system() == "Windows"
    os.system("cls")
    

def mostlist(): #Definiendo la función para mostrar la lista con los números pares e impares
    while True:
        sum = 0
        num = randint(0,20)
        lista.append(num)
        
        if num == 0:
            print(lista[:-1])
            print("Se mostró el número 0, fin del programa", "\n")
            break
    
    print("Presione una tecla para continuar...")
    msvcrt.getch()
    
    print(f"La longitud de la lista es de: ", len(lista[:-1]), "\n") #Usando "len" para mostrar la distancia de la lista
    
    print("Presione una tecla para mostrar los números pares e impares...")
    msvcrt.getch()
    
    #Limpiando el terminal
    platform.system() == "Windows"
    os.system("cls")

    #Añadiendo los números pares e impares en diferentes listas
    for num in lista[:-1]:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print("Números pares: ", pares)
    print("Números impares: ", impares)
    
    #Limpiando la listas par e impar porque ya no se muestran
    pares.clear()
    impares.clear()
            
    print("Presione una tecla para continuar...")
    msvcrt.getch()
            
    platform.system() == "Windows"
    os.system("cls")
    
    
def sumyprom(sum): #Definiendo la función para sumar y mostrar el promedio de la lista
    print("Presione una tecla para ver la suma total y el promedio...")
    msvcrt.getch()
    
                
    for num in lista:
        sum += num #Definiendo la suma
        
    prom = sum/len(lista) #Definiendo el promedio
    print("La suma total de los números es: ", sum)
    print("El promedio total es: ", prom)
    
    

def respuesta(): #Definiendo la función para que el usuario ingrese una respuesta
    resp = None
    while resp != "Y" and resp != "N":
        print("¿Desea generar otra lista? (El programa se reiniciará) (Y/N): ")
        resp = msvcrt.getwch()
        lista.clear() #Limpiando la lista principal porque ya no se muestra
    return resp