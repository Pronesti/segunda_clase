#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:35:02 2019

@author: diego
"""

lista_de_100 =[]
i=0
while i< 100:
    lista_de_100.append(i)
    i +=1

def imprimir_inverso(una_lista):
    nueva_lista = una_lista.copy()
    nueva_lista.reverse()
    return nueva_lista

def imprimir_cada_dos(una_lista):
    i=0
    nueva_lista = []
    while i < 100:
       if i%2 == 0:
           nueva_lista.append(una_lista[i])
       i+=1    
    return nueva_lista
reverso = imprimir_inverso(lista_de_100)
cada_dos = imprimir_cada_dos(lista_de_100)