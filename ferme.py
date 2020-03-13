# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 09:47:19 2020

@author: Damien
"""
import datetime
import random

datetime_today = datetime.datetime.now()

class Animal:
    def __init__(self, number):
        self.sex = random.choice(["mal","femelle"])
        self.age = 0
        self.number = number
        
    def __str__(self):
        return self.sex + " " + str(self.age) + "ans, nombre: " + str(self.number)


if (__name__ == '__main__'):
    mon_dictionnaire = {}
    mon_dictionnaire["Mouton"] = Animal(0, 10)
    mon_dictionnaire["Vache"] = Animal(0, 5)
    print(datetime_today)
    for key, value in mon_dictionnaire.items():
        print (key, value)    
    
    my_delta = datetime.timedelta(365)
    datetime_today += my_delta
    
    print("\n",datetime_today)
    
    for key, value in mon_dictionnaire.items():
        mon_dictionnaire[key].age += 1
        print (key, value)
    
    datetime_today = datetime_today + my_delta
   