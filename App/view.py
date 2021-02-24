"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Videos con más views para una categoría y pais")
    print("3- Video con más dias de trending en un país")
    print("4- Video con más dias de trending para una categoría")
    print("5- Videos con más likes para un tag")


catalog = None

def initCatalog(tipo):
    return controller.initCatalog(tipo)


def loadData(catalog):
    controller.loadData(catalog)

def printFirstVideo(catalog):
    firstVideo = lt.getElement(catalog["videos"], 1)
    print("Titulo: " + firstVideo["title"] + ", Canal: " + firstVideo["channel_title"] +
        ", Dia de tendencia: " + firstVideo["trending_date"] + ", Pais: " + firstVideo["country"] + 
        ", Vistas: " + firstVideo["views"] + ", Likes: " + firstVideo["likes"] + ", Dislikes: " + firstVideo["dislikes"])
    
def printBestViews(videos):
    for n in range (1,lt.size(videos)+1):
        video = lt.getElement(videos, n)
        print("\nDia de tendencia: " + video["trending_date"] + ", Titulo: " + video["title"] +
            ", Canal: " + video["channel_title"] +", Tiempo de publicacion: " +video["publish_time"] +
            ", Vistas: " + video["views"] + ", Likes: " + video["likes"] + ", Dislikes: " + video["dislikes"])

"""
Menu principal
"""
tipo = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tipo = input("Tipo de lista a implementar para el catalogo de videos(ARRAY_LIST o LINKED_LIST): ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog(tipo)
        loadData(catalog)
        print("No. Videos cargados: " + str(lt.size(catalog["videos"])))
        print("No. Categorías cargadas: " + str(lt.size(catalog["categories"])))

        print("\nPRIMER VIDEO CARGADO:")
        printFirstVideo(catalog)
            
        print("\nCATEGORIAS CARGADAS:")
        for n in range(1,lt.size(catalog["categories"])+1):
            print(lt.getElement(catalog["categories"], n))

    elif int(inputs[0]) == 2:
        category_name = None#input("Nombre de la categoria a buscar: ")
        country = None#input("Nombre del pais a buscar: ")
        number = input("Numero de videos a listar: ")
        ordenamiento = input("Tipo de ordenamiento dde datos a implementar(selection, insertion o shell): ")
        if int(number) > lt.size(catalog["videos"]):
            print("Numero de videos a listar muy grande")
        else:
            videos = controller.getBestViews(catalog, category_name, country, int(number), ordenamiento )
            print("TOP " + number + " VIDEOS DE " + str(category_name) + " EN " + str(country) + ":")
            printBestViews(videos)

    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass

    elif int(inputs[0]) == 5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
