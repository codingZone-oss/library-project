import mysql.connector

try:
    conextion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "livraria",
    autocommit = True
    )

except FileNotFoundError:
    print('Data Base not Found')

except FileExistsError:
    print(f'Data Base bank_bd not Existis')

except:
    print('something wrong')
    
cursor = conextion.cursor()

# conextion.close()
