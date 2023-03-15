#hacer un pequeño proyecto que te permita guardar las contraseñas de las 
#páginas o aplicaciones, en un archivo y encriptarlas con un nivel básico de encripación. 

import tkinter
from tkinter.constants import RIGHT
from getpass import getpass

#agregar 

def agregar_cuenta():
    file = open("keys.txt", "a")

    correo = input("Correo: ").strip()
    contraseña = getpass("Contraseña: ").strip()

    l = correo + " " + contraseña 

    file.write(l + "\n")

#consultar una contraseña existente 
    
def consultar():
    a_dictionary = {}
    inp = ""
    a_file = open("keys.txt")
    for line in a_file:
        key, value = line.split()

        a_dictionary[key] = value

    while True: 
        inp = input("Escribe el correo de la constraseña que desea obtener: ").strip()
        if inp in a_dictionary:
            print(f"Su contraseña es: {a_dictionary[inp]}")
            break
        else:
            print("El correo no existe vuelva a ingresarlo. ")



#salir del programa
def salir_programa():
    exit()

window = tkinter.Tk()
window.geometry("400x230")

etiqueta = tkinter.Label(window, text = "Bienvido a tu administrador de contraseñas", bg = "grey")
etiqueta.pack(fill = tkinter.X)

buton1 = tkinter.Button(window, text = "Agregar", padx = 40, pady = 30, command = agregar_cuenta)
buton1.pack()

buton2 = tkinter.Button(window, text = "Consultar", padx = 35, pady = 30, command = consultar)
buton2.pack()

buton3 = tkinter.Button(window, text = "Salir", padx = 45, pady = 20, command = salir_programa)
buton3.pack(side = RIGHT)

window.mainloop()
