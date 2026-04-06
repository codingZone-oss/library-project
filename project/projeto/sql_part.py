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
    

class AddBook():

    def insert(self, title, year, author, price, stock, isbn, publisher, category, nationality, description) -> None:
        try:
            query = """ INSERT INTO livros (titulo, ano_publicacao, autor, preco, estoque, ISBN, editora, categoria, nacionalidade, descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
            cursor.execute(query, (title, year, author, price, stock, isbn, publisher, category, nationality, description))

        except Exception as e:
            print("ERROR IN ADDING BOOKS:", e)

        else:
            print("BOOKS ADDED WITH SUCCESS")


class UpdateBooks:
    
    def update(self, cod:int, title, year, author, price, stock, isbn, publisher, category, nationality, description) -> str:
        try:
            query = """ UPDATE livros SET titulo = %s, ano_publicacao = %s, autor = %s, preco = %s, estoque = %s, ISBN = %s, editora = %s, categoria = %s, nacionalidade = %s, descricao = %s WHERE id = %s;"""
            cursor.execute(query, (title, year, author, price, stock, isbn, publisher, category, nationality, description, cod))

        except Exception as e:
            print("ERROR IN UPDATING BOOKS:", e);return False
        else:
            print("BOOKS UPDATED WITH SUCCESS");return True

class DeleteBooks():
    
    def delete(self, id_books:int):
        try:
            cursor.execute("DELETE FROM livros WHERE id = %s", (id_books,))
            
        except Exception as e:
            print("ERROR IN DELETING BOOKS:", e);return False
        else:
            print("BOOKS DELETED WITH SUCCESS");return True
        
class Readers() :

    def __init__(self):
        pass

    def select_count_readers(self):
        cursor.execute("SELECT COUNT(id) FROM leitores")
        for line in cursor:
            values = line
        return values
    
    def select_readers(self, value) -> None:

        query = (f' select id, nome, email, telefone, nacionality, city, number_identity, library_card_ticket from leitores where nome like "%{value}%"')

        try:
            cursor.execute(query)
        except Exception as e:
            print(f"ERROR EXECUTE QUERY: {e}"); return False
        else:
            return cursor.fetchall(); True

