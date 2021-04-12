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
from PyQt5 import QtWidgets

#%%

class MyApp(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        ## Sin Layouts
        # self.my_label = QtWidgets.QLabel('Hola, esta es nuestra primera Label', self)
        # self.my_label.setGeometry(30, 30, 180, 20)
        # self.my_button = QtWidgets.QPushButton('Mi Primer Botón')
        # self.my_button.setGeometry(50, 40, 100, 20)
        
        ## Con Layouts
        self.my_label = QtWidgets.QLabel('Hola, esta es nuestra primera Label')
        self.my_button = QtWidgets.QPushButton('Mi Primer Botón')
        ## Generamos una Layout Vertical
        layout = QtWidgets.QVBoxLayout()
        
        ## UBICAMOS la Layout en la widget
        self.setLayout(layout)
        
        ## AÑADIMOS las widgets dentro de la Layout
        layout.addWidget(self.my_label)
        layout.addWidget(self.my_button)
        

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
