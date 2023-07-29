import Laboratorio_3 as Lab

print("Bienvenido al programa chistes de Chuck Norris")

chiste = " "  #inicializando la variable chiste

#--------------------------------------Funcion para Mostrar el chiste al usuario------------------------------------------------------
def Mostrar_chiste(opcion):
    global chiste    ## Declarando la variable chiste como un variable global para poder cambiar su valor dentro de la funcion
    opcion = chiste
    if opcion == 1:
        Lab.getRandom()
    elif opcion == 2:
        Lab.getCategories()
                
    elif opcion == 3:
        chiste='Salir'
        print('\nEsperamos que haya disfrutado los chistes de Chuck Norris\n .....Saliendo.\n..\n...\n....\n')
            #elegir_chiste(continua)
    else:
        print("\nOpcion no valida\n")


#--------------------------------------Funcion para pedir la opcion de chiste al usuario----------------------------------------------
def elegir_chiste(): 
    global chiste 

    while chiste != 'Salir':   
        
        try:        ##usando try y except para capturar cuando el usuario ingresa un dato diferente a un numero
            chiste=int(input("""1: Chiste de Chuck Norris Aleatorio
2: Chiste de Chuck Norris por categoria 
3: Salir
>> """))
            Mostrar_chiste(chiste)    
        
        except ValueError:
            print("\nOpcion no valida, por favor ingresa un valor valido")    


#---------------------------------------------------------- Funcion Main  ------------------------------------------------------------
if __name__ == '__main__':
    elegir_chiste()








    #continua = "Continuar"  #inicializando la variable chiste
#