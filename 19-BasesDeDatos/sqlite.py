import sqlite3

###     Conexión
conexion = sqlite3.connect('pruebas.db')

###     Crear cursor
cursor = conexion.cursor()

###     Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo VARCHAR(255),"+
"descripcion TEXT,"+
"precio INT(255)"+
")")

####### Otra forma de escribir la consulta
#cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
#"id INTEGER PRIMARY KEY AUTOINCREMENT,
#"titulo VARCHAR(255),
#"descripcion TEXT,
#"precio INT(255)
#)""")


###     Guardar cambios
conexion.commit()

###     Insertar Datos
"""
cursor.execute("INSERT INTO productos VALUES(null,'Primer producto','Descripcion del producto',550)")
conexion.commit()
"""

###     Insertar varios registros
"""
productos = [
    ("Laptop","Ordenador portatil",15000),
    ("PC","Ordenador de escritorio",32000),
    ("Memoria RAM","Componente",350),
    ("Impresora","Material oficia",5400),
    ("Silla","Material oficina",2700),
    ("Libreta","Cuaderno A2",20),
    ("Teclado","Teclado USB",220),
    ("Mouse","Raton optico",250),
    ("Bocinas","Bocinas USB",320),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()
"""
### Actualizar
cursor.execute("UPDATE productos SET precio=500 WHERE precio = 20")

###     Lectura de datos
#cursor.execute("SELECT * FROM productos;")
cursor.execute("SELECT * FROM productos WHERE precio>=400;")
print(cursor)
productos = cursor.fetchall()
print(productos)

for producto in productos:
    #print(producto)
    print("ID:  ",producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ",producto[2])
    print("Precio: ", producto[3])
    print("---------------------------------------")

cursor.execute("SELECT titulo,precio FROM productos;")
producto = cursor.fetchone() #Obtener el primer registro
print(producto)

###     Borrar registros
"""
cursor.execute("DELETE FROM productos")    #Vaciar la tabla
conexion.commit()
"""

###     Cerrar conexión
conexion.close()