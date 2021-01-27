"""
mysql connector python
mariadb connector python 
postgresql connector python

pypi.org
pip install mysql-connector-python
http://localhost:8080/phpmyadmin/index.php
"""
import mysql.connector

#############################################  Conexion 
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "curso_python"
)

############################################# ¿Conexion correcta?
#print(database)

############################################# Crear Base de datos si no existe
cursor =database.cursor(buffered=True) #buffered=True para evitar fallos al hacer varias activdades con cursor
cursor.execute("CREATE DATABASE IF NOT EXISTS curso_python")

############################################# Listar bases de datos
"""
cursor.execute("SHOW DATABASES")
for bd in cursor:
    print(bd)
"""

############################################# Crear Tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")

############################################# Mostrar tablas
"""
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)
"""

############################################# Inserar datos
"""
coches = [
    ("Seat","Ibiza",25000),
    ("Reanult","Clio",33000),
    ("Citroen","Saxo",45000),
    ("Mercedez","Clase C",32000)
]
"""
#cursor.execute("INSERT INTO vehiculos VALUES (null,'Opel','Astra',18500)")
#cursor.executemany("INSERT INTO vehiculos VALUES (null,%s,%s,%s)",coches)
#database.commit() 


############################################# Eliminar registro
"""
cursor.execute("DELETE FROM vehiculos WHERE marca ='Reanult'")
database.commit()
print(cursor.rowcount,"Borrados !!!") #Total de registros eliminados 
"""
############################################# Actualizar datos
"""
cursor.execute("UPDATE vehiculos SET modelo='Leon' WHERE marca='Seat' ")
database.commit()
print(cursor.rowcount," Actualizados !!!") #Total de registros actualizados
"""

############################################# Hacer consulta

cursor.execute("SELECT * FROM vehiculos")
#cursor.execute("SELECT * FROM vehiculos WHERE precio <= 40000 AND  marca != 'Seat' ")
result = cursor.fetchall()

print("---  TODOS LOS COCHES  ---")
for coche in result:
    print(coche) #print(coche[1],coche[3])
"""
cursor.execute("SELECT * FROM vehiculos")
primer = cursor.fetchone()
print(primer)
"""
