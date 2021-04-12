# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 18:14:41 2021

@author: 
            Alejandro Condori
         Mgter. en Física Médica 
         
    TITULO : Layout Management
"""
#%% 

## IMPORTAMOS los paquetes necesarias.
import sys
from PyQt5 import QtWidgets, QtCore

#%%

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.my_label = QtWidgets.QLabel('Hola, esta es nuestra primera Label')
        self.my_label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        self.my_button_1 = QtWidgets.QPushButton('Mi Primer Botón')
        self.my_button_2 = QtWidgets.QPushButton('Mi Segundo Botón')
        
        ## Generamos una Layout Vertical y una Horizontal
        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        
        ## UBICAMOS la Layout en la widget
        self.setLayout(layout1)
        
        ## AÑADIMOS la label y la segunda layout dentro de la primera Layout
        layout1.addWidget(self.my_label)
        layout1.addLayout(layout2)
        
        ## AÑADIMOS los botones en la segunda layout
        layout2.addWidget(self.my_button_1)
        layout2.addWidget(self.my_button_2)
        
        self.my_button_1.clicked.connect(self.button_1_clicked)
        self.my_button_2.clicked.connect(self.button_2_clicked)
        

    def button_1_clicked(self):
        print('El primer botón fue presionado')

    def button_2_clicked(self):
        print('El segundo botón fue presionado')  

#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
