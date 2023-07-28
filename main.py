import Laboratorio_3 as Lab

def Mostrar_chiste():
    chiste = ' '
    while chiste != 'salir':
        chiste=int(input("Deseas optener un chiste de Chuck Norris? \n\n Por favor escoja una opcion \n 1: Chiste de Chuck Norris Aleatorio\n 2: Chiste de Chuck Norris por categoria \n 3: Salir \n>> "))
        #chiste=int(chiste)
        if chiste == 1:
            Lab.getRandom()
        elif chiste == 2:
            Lab.getCategories()
        
        elif chiste == 3:
            chiste='salir'
            print('\nEsperamos que haya disfrutado los chistes de Chuck Norris\n .....Saliendo.\n..\n...\n....\n')

        else:
            print("\nOpcion no valida")



if __name__ == '__main__':
    Mostrar_chiste()