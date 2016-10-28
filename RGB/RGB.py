#!/usr/bin/env python
# -*- coding: utf-8 -*-

##########################################################
# Script de python para controlar un led RGB a través de #
# la interfaz gráfica Tkinter, el puerto serie y Arduino #
#                                                        #
# Autor: Raúl Hurtado Gavilán                            #
# Fecha: 2016/08/21                                      #
# Licencia: GPL                                          #
# Versión: 1.0                                           #
##########################################################

from Tkinter import *
import serial
import time

puertoSerie = '/dev/ttyUSB0' # Puerto serie de Linux donde está Arduino. Buscar en cada caso
ratio = 9600 # Velocidad de la comunicación serie. Se puede modificar
ser = serial.Serial(puertoSerie, ratio, timeout = 1, writeTimeout = 1)
time.sleep(1)

Ventana = Tk() # Se crea la ventana
Ventana.wm_title("Control RGB") # Título de la ventana

def cerrar(): # Método para cerrar la ventana. Se encuentra en el botón
	Ventana.destroy()

#Texto principal
Label(text = "Programa para controlar el color de un led RGB\nmediante sliders y PWM en Arduino").grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)

#Sliders y etiquetas
rojo = Scale(from_= 0, to = 255, orient = HORIZONTAL)
rojo.grid(row = 1, column = 1)

Label(text = "Control color rojo").grid(row = 1, column = 0)

verde = Scale(from_= 0, to = 255, orient = HORIZONTAL)
verde.grid(row = 2, column = 1)

Label(text = "Control color verde").grid(row = 2, column = 0)

azul = Scale(from_= 0, to = 255, orient = HORIZONTAL)
azul.grid(row = 3, column = 1)

Label(text = "Control color azul").grid(row = 3, column = 0)

b = Button(text = 'Cerrar', command = cerrar).grid(row = 4, columnspan = 2)


#Serial
serBuffer = ''
while True:
	ROJO = 'r' + str(rojo.get())
	VERDE = 'g' + str(verde.get())
	AZUL = 'b' + str(azul.get())
	#print ROJO
	ser.write(ROJO)
	time.sleep(0.01)
	ser.write(VERDE)
	time.sleep(0.01)	
	ser.write(AZUL)
	time.sleep(0.01)
	Ventana.update()

Ventana.mainloop()


