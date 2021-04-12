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
        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QHBoxLayout()
        self.setLayout(layout1)
        layout1.addWidget(self.my_label)
        layout1.addLayout(layout2)
        layout2.addWidget(self.my_button_1)
        layout2.addWidget(self.my_button_2)
        self.my_spin_box = QtWidgets.QSpinBox()
        layout1.addWidget(self.my_spin_box)
        self.my_spin_box.setMaximum(100)
        self.my_spin_box.setMinimum(-100)
        self.my_spin_box.setSingleStep(10)
        self.my_spin_box.setPrefix("Temp = ")
        self.my_spin_box.setSuffix("°C")
        self.my_spin_box.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        
        ## GENERAMOS una instancia de la clase QDoubleSpinBox y la añadimos a la 
        ## layout 1
        self.my_double_spin = QtWidgets.QDoubleSpinBox()
        layout1.addWidget(self.my_double_spin)
        
        ## Realizemos algunas modificaciones
        self.my_double_spin.setMaximum(200.00)
        self.my_double_spin.setMinimum(-200.00)
        self.my_double_spin.setSingleStep(2.5)
        self.my_double_spin.setValue(32.00)
        self.my_double_spin.setPrefix("Temp = ")
        self.my_double_spin.setSuffix("°F")
        self.my_double_spin.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)
        
        ## Conectemos la señal de modificación de valor
        self.my_spin_box.valueChanged.connect(self.spin_changed)
        
        self.my_button_1.clicked.connect(self.button_1_clicked)
        self.my_button_2.clicked.connect(self.button_2_clicked)

    def button_1_clicked(self):
        print('El primer botón fue presionado')

    def button_2_clicked(self):
        print('El segundo botón fue presionado')

    def spin_changed(self, val):
        Fahr = 9.0/5*val+32
        self.my_double_spin.setValue(Fahr)


#%%

## GENEREMOS una instancia de la clase que hemos creado, la base necesaria y la
##     ejecutamos.
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
