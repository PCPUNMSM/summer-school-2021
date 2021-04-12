# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO BASE
"""
#%%

class Mi_Primera_Clase():
    pass

Mi_Primer_Objeto = Mi_Primera_Clase()
print( Mi_Primer_Objeto )
# Output: 
# <__main__.Mi_Primera_Clase object at 0x000001DD462994C0>

#%%

class Ser_Humano():
    edad = 0
    huesos = 206
    manos = 2 
    pies = 2
    ojos = 2 
    
Pepe = Ser_Humano()
print(Pepe.edad, Pepe.ojos)
# Output:
# 0 2

#%%

Pepe.edad = Pepe.edad + 1
print(Pepe.edad)
# Output:
# 1

#%%

Juan = Ser_Humano()
Juan.edad = 20
print(Pepe.edad, Juan.edad)# Output:
# 1 20

#%%

class Ser_Humano_2():
    edad = 0
    def crecio(self):
        self.edad += 1

Lucas = Ser_Humano_2()
Lucas.crecio()
print(Lucas.edad)
Lucas.crecio()
print(Lucas.edad)
Lucas.crecio()
print(Lucas.edad)
# Output:
# 1
# 2
# 3

#%%

class Ser_Humano_3():
    edad = 0 
    def __init__(self, ojos, cabello):
        self.eye_color = 'Ojos ' + ojos
        self.hair_color = 'Cabello ' + cabello

    def crecio(self):
        self.edad += 1

Jose = Ser_Humano_3('Negros', 'Marrón')
print(Jose.eye_color, Jose.hair_color)
# Output:
# Ojos Negros Cabello Marrón
Jose.crecio()
print(Jose.edad)
# Output:
# 1

#%%

class Ser_Humano_4( Ser_Humano_3 ):
    def __init__(self, ojos, cabello):
        Ser_Humano_3.__init__(self, ojos, cabello)
        self.enamorado = False

    def enamorarse(self):
        self.enamorado = True

Sam = Ser_Humano_4('Azules', 'Rubio')

for i in range(25):
    Sam.crecio()
Sam.enamorarse()

if Sam.enamorado:
    print('Oh no, se enamoró')
    print(f'Tiene {Sam.edad} años')
    