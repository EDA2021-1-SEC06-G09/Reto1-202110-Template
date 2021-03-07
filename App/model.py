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
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
import time



# Construccion de modelos
def newCatalog():
    catalog = {'videos': None,
               'categories': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = lt.newList('ARRAY_LIST', cmpfunction=comparecat)

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
def binarySearch(lst, elemento):
    i = 0
    f = len(lst)-1
    pos = -1
    found = False
    while i <= f and not found:
        m = (i+f)//2
        if lst[m] == elemento:
            pos = m
            found = True
        elif lst[m] > elemento:
            f = m-1
        else:
            i = m+1
    return pos


def getCategoryId(catalog, category_name):
    for n in range(1,lt.size(catalog["categories"])+1):
        category = lt.getElement(catalog["categories"], n)
        if category["name"].lower() == category_name.lower():
            return category["id"]
    return None



def getBestViews(catalog, category_id, country):
    listcopy = catalog["videos"].copy()
    sorted_list = sortVideoCountry(listcopy)

    return sortVideoViews(sorted_list)

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecat(cat1, cat):
    if (cat1 in cat['id']):
        return 0
    return -1


def cmpVideosByViews(video1, video2):
    return (int(video1["views"]) > int(video2["views"]))


def cmpVideosByCountryCategory(video1, video2):
    return ((video1["country"] < video2["country"]) and (video1["category_id"] < video2["category_id"]))


# Funciones de ordenamiento

def sortVideoCountry(videos):
    return merge.sort(videos, cmpVideosByCountryCategory)


def sortVideoViews(listcopy):    
    sorted_list = quick.sort(listcopy, cmpVideosByViews)
    return sorted_list
