## Laboratorio 3 
## Consumo de una API publica de chistes de Chuck Norris


##Funcion para solicitar un chiste aleatorio al servidor
import requests

url = 'https://api.chucknorris.io/jokes/random'

## Usando el metodo GET
def getRandom():
    getResponse = requests.get(url)

    if getResponse.status_code == 200:
        data = getResponse.json()
        print(getResponse.status_code)
        print("Respuesta del servidor")
        print(data["value"])

    else:
        print('Error al realizar la solicitud')
        print(getResponse.status_code)


##Obtener la lista de categoria de chistes y solicitar al usuario la categoria solicitada
url1 = "https://api.chucknorris.io/jokes/categories"

def getCategories():
    getCtgrs=requests.get(url1)

    if getCtgrs.status_code == 200:
        categories = getCtgrs.json()
        print("\n\nEl codigo de respuesta es: ", getCtgrs.status_code)
        print("Las categorias de los chistes son: ")
        for i in categories:
            print(i)
        opcion=str(input('Por favor digite una categoria \n'))
        Chiste_Categoria(opcion)

    else:
        print('Error al realizar la solicitud')
        print(getResponse.status_code)

def Chiste_Categoria(Option):
    url3='https://api.chucknorris.io/jokes/random?category='
    arg=Option
    ##uniendo la url y el parametro para completar la url de la categoria escogida por el usuario
    url4=url3 + arg
    getchiste=requests.get(url4)  
    
    if getchiste.status_code == 200:
        chiste=getchiste.json()
        print("\n\n El chiste de la categoria",Option , "es: \n", chiste["value"], "\n ja ja ja ja ja")

    else:
        print("Solicitud denegada", getchiste.status_code)

if __name__ == '__main__':
    chiste = ' '
    while chiste != 'salir':
        chiste=int(input("Este programa le mostrara chistes de Chuck Norris \n\n Por favor escoja \n 1: Chiste de Chuck Norris Aleatorio\n 2:Chiste de Chuck Norris por categoria \n"))
        if chiste == 1:
            getRandom()
        elif chiste == 2:
            getCategories()

        else:
            print("Opcion no valida")
 