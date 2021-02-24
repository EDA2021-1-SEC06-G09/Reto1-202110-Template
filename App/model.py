"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import subList
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as shell
from DISClib.Algorithms.Sorting import selectionsort as selection
from DISClib.Algorithms.Sorting import insertionsort as insertion
assert cf
import time



# Construccion de modelos
def newCatalog(tipo):
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList(tipo)
    catalog['categories'] = lt.newList("ARRAY_LIST", cmpfunction=comparecat)

    return catalog

# Funciones para agregar informacion al catalogo
def addvideo(catalog, video):
    lt.addLast(catalog["videos"], video)


def addcategory(catalog, cat):  
    poscat = lt.isPresent(catalog["categories"], cat["id"])

    if poscat == 0:
        c = newcategory(cat["name"].strip(), cat["id"])
        lt.addLast(catalog["categories"], c)


# Funciones para creacion de datos
def newcategory(name, id):
    cat = {"id": "", "name":""}
    cat["id"] = id
    cat["name"] = name
    return cat


# Funciones de consulta
def getBestViews(catalog, category_name, country, sample, ordenamiento):

    return sortVideoViews(catalog, ordenamiento, sample)

# Funciones utilizadas para comparar elementos dentro de una lista
def comparecat(cat1, cat):
    if (cat1 in cat['id']):
        return 0
    return -1

def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) > int(video2["views"]))


# Funciones de ordenamiento
def sortVideoViews(catalog, ordenamiento, size):
    sub_list = lt.subList(catalog["videos"], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    
    if ordenamiento == "shell":
        sorted_list = shell.sort(sub_list, cmpVideosByViews)
    elif ordenamiento == "selection":
        sorted_list = selection.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = insertion.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time) *1000
    return elapsed_time_mseg, sorted_list
