from conection_DB import collection
import json

def read_productos(id=None):
    if id is not None:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)

def read_producto(nombre=None):
    if nombre is not None:
        query = {"nombre": nombre}
        document = collection.find_one(query)
        print(document)
    else:
        print("El producto no existe...")

def create_productos(json_productos):
    result = collection.insert_one(json_productos)
    print("Producto añadido correctamente:",result.acknowledged)

def update_productos(nombre, json_productos_update):
    query = {"nombre": nombre}
    new_values = {"$set": json_productos_update}
    result = collection.update_one(query,new_values)
    print("Productos modificados:",result.modified_count)

def delete_productos(nombre):
    query = {"nombre": nombre}
    result = collection.delete_one(query)
    print("Productos eliminados:",result.deleted_count)