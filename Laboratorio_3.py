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
        #print(getResponse.status_code)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(data["value"])
        print("ja ja ja ja \n--------------------------------------------------------\n")

    else:
        print('\nError al realizar la solicitud')
        print(getResponse.status_code)


##Obtener la lista de categoria de chistes y solicitar al usuario la categoria solicitada
url1 = "https://api.chucknorris.io/jokes/categories"

def getCategories():
    getCtgrs=requests.get(url1)

    if getCtgrs.status_code == 200:
        categories = getCtgrs.json()
        print("Las categorias de los chistes son: ")
        for i in categories:
            print(i)
        opcion=str(input('Por favor digite una categoria \n'))
        Chiste_Categoria(opcion)

    else:
        print('\nError al realizar la solicitud\n')
        

def Chiste_Categoria(Option):
    url3='https://api.chucknorris.io/jokes/random?category='
    arg=Option
    ##uniendo la url y el parametro para completar la url de la categoria escogida por el usuario
    url4=url3 + arg
    getchiste=requests.get(url4)  
    
    if getchiste.status_code == 200:
        chiste=getchiste.json()
        print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n El chiste de la categoria",Option , "es: \n", chiste["value"], "\n ja ja ja ja ja\n--------------------------------------------------------\n\n")

    else:
        print("Solicitud denegada", getchiste.status_code)


    
 