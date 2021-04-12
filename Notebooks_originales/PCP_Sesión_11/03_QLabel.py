# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO DE QLABEL
"""
#%% 

## IMPORTAMOS los paquetes necesarias.
import sys
from PyQt5 import QtWidgets

#%%

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        ## GENERAMOS una instancia de la clase QLabel 
        self.my_label = QtWidgets.QLabel('Hola, esta es nuestra primera Label', self)
        
        ## POSICIONAMOS la label
        self.my_label.setGeometry(150, 40, 400, 20)
        print(self.my_label.alignment())
        
        

#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
