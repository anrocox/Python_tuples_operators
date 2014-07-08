#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 7, 2014

@author: anroco

How operators + and * are used with a python tuple?

¿Como se usan los operadores + y * con una tupla python?
'''

#create a tuple
tupla = 2,

#The * operator allow repeat the items in the tuple
print(tupla * 5)

#create a tuple with repeated items.
tupla = (1, 2, 3) * 3
print(tupla)

#create three tuples
tupla1 = (2, 4, 8, 16, 32, 64)
tupla2 = ('a', 'b', 'c', 'd')
tupla3 = (True, False)

#The + operator allow create a tuple joining two or more tuples
tupla = tupla1 + tupla2 + tupla3
print(tupla)
