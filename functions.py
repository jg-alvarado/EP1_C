def create_json_productos():
    nombre = input("Nombre: ")
    precio = int(input("Precio: "))
    cantidad = input("Cantidad: ")
    categoria = input("Categoria: ")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria,
    }

    return producto

def create_json_update():
    print("Menu de opciones")
    print("1) Modificar todos los datos del documento")
    print("2) Modificar un elemento del documento")
    opcion = input("Eliga una opcion: ")
    if opcion == "1":
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        cantidad = input("Cantidad: ")
        categoria = input("Categoria: ")

        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria,
        }

        return producto
    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        producto = {indice: valor}
        return producto
    else:
        print("Dato ingresado no valido")

def delete_json_productos():
    confirmacion = input("Esta seguro de eliminar el siguiente producto? ")
    producto = {confirmacion}
    return producto

