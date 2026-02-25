from class_conextion import cursor

class SqlParts():
    
    def __init__(self, query:str) -> None:
        self.query = query

    def execute(self, values:tuple) -> None:
        try:
            cursor.execute(self.query, values)
        
        except Exception as e:
            print("ERROR IN SQL EXECUTION:", e)


    def select_books(self):
        cursor.execute("SELECT COUNT(id) FROM livros")
        for line in cursor:
            values = line
        return values

    def select_workers(self):
        cursor.execute("SELECT COUNT(id) FROM worker")
        for line in cursor:
            values = line
        return values
    
    def select_readers(self):
        cursor.execute("SELECT COUNT(id) FROM clientes")
        for line in cursor:
            values = line
        return values
    

class AddBook():

    def insert(self, title, year, author, price, stock, isbn, publisher, category, nationality, description) -> None:
        try:
            query = """ INSERT INTO livros (titulo, ano_publicacao, autor, preco, estoque, ISBN, editora, categoria, nacionalidade, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
            cursor.execute(query, (title, year, author, price, stock, isbn, publisher, category, nationality, description))

        except Exception as e:
            print("ERROR IN ADDING BOOKS:", e)

        else:
            print("BOOKS ADDED WITH SUCCESS")


class UpdateBooks():
    
    def update(self, cod:int, title:str, year:int, price:float, stock:int) -> None:
        try:
            query = """UPDATE livros SET titulo = %s, ano_publicacao = %s, preco = %s, estoque = %s WHERE (id = %s);"""
            cursor.execute(query, (title, year, price, stock, cod))

        except Exception as e:
            print("ERROR IN UPDATING BOOKS:", e)
        else:
            print("BOOKS UPDATED WITH SUCCESS")


class DeleteBooks():
    
    def delete(self, id:int):
        try:
            query = """DELETE FROM livros WHERE (id = %s);"""
            cursor.execute(query, (id))
            
        except Exception as e:
            print("ERROR IN DELETING BOOKS:", e)
        else:
            print("BOOKS DELETED WITH SUCCESS")