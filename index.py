from crud import *
from functions import *

while True:
    print("Menu de opciones")
    print("1) Ver todos los productos.")
    print("2) Buscar un producto")
    print("3) Agregar un producto")
    print("4) Modificar un producto")
    print("5) Eliminar un producto")
    print("6) Salir del sistema")
    opcion = input("Eliga una opcion: ")
    if opcion == "1":
        read_productos()
    elif opcion == "2":
        nombre = input("Eliga el producto a buscar: ")
        read_producto(nombre)
    elif opcion == "3":
        producto = create_json_productos()
        create_productos(producto)
    elif opcion == "4":
        nombre = input("Eliga el producto a modificar: ")
        producto = create_json_update()
        update_productos(nombre, producto)
    elif opcion == "5":
        nombre = input("Eliga el producto a eliminar: ")
        producto = delete_json_productos()
        delete_productos(nombre)
    elif opcion == "6":
        print("Gracias por visitar el sistema")
        exit()
