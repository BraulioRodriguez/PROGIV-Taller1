## Programacion de Computadoras IV
# Diccionario de Slang Panameño - TALLER I
# Braulio Rodriguez 8-899-1093

import sqlite3

# Conexion o creacion de base de datos
conn = sqlite3.connect('slangs.db')

# Creacion de objeto cursor
cur = conn.cursor()

# Creacion de tabla
cur.execute("""CREATE TABLE IF NOT EXISTS slangs(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               palabra TEXT NOT NULL,
               significado TEXT NOT NULL);""")


# Funcion de Insertar

def insertData(palabra, significado):
    qry = 'INSERT INTO slangs (PALABRA, SIGNIFICADO) values(?,?);'
    conn.execute(qry, (palabra, significado))
    conn.commit()
    print("Datos agregados exitosamente.")

# Funcion de Editar

def updateData(palabra, significado):
    qry = 'UPDATE slangs SET palabra=?, significado=? WHERE palabra=?;'
    conn.execute(qry, (palabra, significado, palabra))
    conn.commit()
    print("Datos editados exitosamente.")

# Funcion de Borrar

def deleteData(id):
    qry = 'DELETE FROM slangs WHERE palabra=?;'
    conn.execute(qry, (palabra,))
    conn.commit()
    print("Datos eliminados exitosamente.")

# Funcion de Ver lista

def selectData():
    qry = 'SELECT * FROM slangs'
    resultado = conn.execute(qry)
    for i in resultado:
        print(i)

# Funcion de Buscar Significado

def searchData(palabra):
    qry = 'SELECT significado FROM slangs WHERE palabra=?'
    resultado = conn.execute(qry, (palabra,)).fetchone()
    if resultado is None:
        print("No se encontro la palabra.")
    else:
        print(resultado[0])

conn.commit()


# Menu de opciones
print("""
1. Insertar
2. Editar
3. Borrar
4. Visualizar
5. Buscar
6. Salir
""")

# Programa Principal

resp = 1
while resp == 1:
    opcion = int(input("Ingrese una opcion: "))

    if(opcion == 1):
        print("Ingresar nuevo registro")
        palabra = input("Ingrese un slang panameno: ")
        significado = input("Ingrese su significado: ")
        insertData(palabra, significado)

    elif(opcion == 2):
        print("Edite un registro: ")
        id = input("Ingrese el ID: ")
        palabra = input("Ingrese un slang panameno: ")
        significado = input("Ingrese su significado: ")
        updateData(palabra, significado)

    elif opcion == 3:
        print("Borre un registro")
        id = input("Ingrese el ID: ")
        deleteData(id)

    elif opcion == 4:
        print("Ver listado de palabras")
        selectData()

    elif opcion == 5:
        print("Buscar significado de palabra")
        palabra = input("Ingrese un slang panameno: ")
        searchData(palabra)

    elif opcion == 6:
        break

    else:
        print("ERROR! OPCION INVALIDA")

    resp = input("Si desea continuar presione [1]")



