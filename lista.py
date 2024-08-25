#Fecha: 06/05/2024
#Centro de Biotecnología Agropecuario
#Ficha: 2877795
#Aprendiz: Nicolás Agamez Melo
#Versión 3.12.3

import Modules.functions01 as functions01


def main(): #Definiendo la función inicial
    
    #Definiendo las listas
    lista = []
    pares = []
    impares = []
    sum = 0
    
    resp = "Y"

    while resp == "Y": #Si la respuesta del usuario es "Y" se repite el proceso
        
        
        #Llamando las funciones
        functions01.ingreso()

        functions01.mostlist()

        functions01.sumyprom(sum)

        resp=functions01.respuesta()
        

if __name__=="__main__": #Ejecutando la función principal
    main()