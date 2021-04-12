# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : EJEMPLO DE QPUSHBUTTON
"""
#%% 

## IMPORTAMOS los paquetes necesarias.
import sys
from PyQt5 import QtWidgets

#%%

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.my_label = QtWidgets.QLabel('Hola, esta es nuestra primera Label', self)
        self.my_label.setGeometry(20, 20, 180, 20)

        ## GENERAMOS una instancia de la clase QPushButton
        self.my_button = QtWidgets.QPushButton('Mi Primer Botón', self)
        
        ## POSICIONAMOS el botón
        self.my_button.setGeometry(50, 40, 100, 20)
        
        ## CONECTAMOS la señal de click con un método
        self.my_button.clicked.connect(self.button_clicked)
        

    def button_clicked(self):
        print('El botón fue presionado')        

#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
