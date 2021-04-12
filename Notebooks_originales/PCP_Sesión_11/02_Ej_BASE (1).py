# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO BASE
"""
#%% 

## IMPORTAMOS los paquetes necesarias.
import sys
from PyQt5 import QtWidgets

#%%

## GENEREMOS la clase que defina la GUI
class MyApp(QtWidgets.QWidget):
    ## CREAMOS el constructor de la clase
    def __init__(self):
        ## HEREDAMOS los atributos y métodos de la clase QWidget llamando su
        ##    constructor
        QtWidgets.QWidget.__init__(self)
        ## Hasta aqui generamos una subclase idéntica a la clase QWidget

#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
