#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:36:43 2019

@author: diego
"""

#Sumatoria de todos los numeros de la lista
#lista[0]+lista[1]+lista[2]+...
def sumatoria(lista):
    i=len(lista)-1
    total=0
    while i >= 0:
        total += lista[i]
        i-=1
    return total

edades = [22, 24, 44, 33]
print(sumatoria(edades))
# 123


#me devuelve la lista modificada con todos los numeros
#multiplicados por "multiplo"
def duplicar_todo_por(lista, multiplo):
    i=len(lista)-1
    while i >= 0:
        lista[i] = lista[i] * multiplo
        i-=1
    return lista

numeros = [1, 2, 3]
duplicar_todo_por(numeros, 3)
print(numeros)
# [3, 6, 9]


#Te devuelve si numero esta dentro de la lista
def esta_en_lista(lista, numero):
    i=len(lista)-1
    while i >=0:
        if lista[i] == numero:
            return True
        i-=1
    return False

codigo_de_cursos = ["aka101", "php", "carpinteria"]

if esta_en_lista(codigo_de_cursos, "carpinteria"):
    print("Genial, existe el curso de carpinteria")
else:
    print("Mmmm, no deberia imprimir esto")

if esta_en_lista(codigo_de_cursos, "cafeteria"):
    print("Mmmm, no deberia imprimir esto")
else:
    print("Claro, no hay curso de cafeteria :( ")