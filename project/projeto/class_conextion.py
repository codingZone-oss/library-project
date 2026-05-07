import mysql.connector

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="livraria",
        autocommit=True
    )
except FileNotFoundError:
    print('Data Base not Found')
except FileExistsError:
    print('Data Base bank_bd not Existis')
except mysql.connector.Error as e:
    print(f'Something unexpected happened: {e}')
except Exception as e:
    print(f'Unexpected error: {e}')
else:
    cursor = connection.cursor()
