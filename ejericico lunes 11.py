# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 19:56:01 2021

@author: User
"""

Lista= [12,23,5,29,92,64]

def Change (lista=[],a=-1, b=0):
    lista.insert(b,lista.pop(a))
    return (lista)
    
print(Change(Lista))
print(Change(Lista,1,-1))
Lista.insert(0,14)
print(Lista)
Lista.append(sum(Lista))
print(Lista)
Lista+=[4,11,32]
print(Lista)
Lista2=[]

for i in range(len(Lista)):
    if (Lista[i])%2!=0:
        Lista2.append(Lista[i])
for i in range(len(Lista2)):
    Lista.remove(Lista2[i])
 
print(Lista)
Lista.sort()
print(Lista)
Lista.clear()
print(Lista)