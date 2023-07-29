## Laboratorio 3 
## Consumo de una API publica de chistes de Chuck Norris

import requests

##-------------------------Funcion para solicitar un chiste aleatorio al servidor----------------------------------

url = 'https://api.chucknorris.io/jokes/random'

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



##---------------- Funcion para obtener la lista de categorias de chistes y solicitar al usuario la categoria solicitada ----------------------
url1 = "https://api.chucknorris.io/jokes/categories"

def getCategories():
    getCtgrs=requests.get(url1)

    if getCtgrs.status_code == 200:
        categories = getCtgrs.json()
        print("Las categorias de los chistes son: ")
        for i in categories:
            print(i)
        categ=str(input('Por favor digite una categoria \n'))
        Chiste_Categoria(categ)

    else:
        print('\nError al realizar la solicitud\n')
        


##------------------------Funcion para obtener el chiste segun categorias escogida por el usuario ---------------------------------
def Chiste_Categoria(categ_chiste):
    url3='https://api.chucknorris.io/jokes/random?category='
    category=categ_chiste
    ##uniendo la url y el parametro para completar la url de la categoria escogida por el usuario
    url4=url3 + category
    getchiste=requests.get(url4)  
    
    if getchiste.status_code == 200:
        chiste=getchiste.json()
        print("\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n ", chiste["value"], "\n ja ja ja ja ja\n--------------------------------------------------------\n\n")

    else:
        print("\nERROR ------->", categ_chiste, "no es una categoria valida, por favor escoje una opcion valida\n")


    
 