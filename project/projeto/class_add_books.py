from class_conextion import cursor
from classs_warning_frame import Alert, Successefull

class AddBook():

    def insert(self, title, year, price, stock) -> None:
        try:
            query = """
                INSERT INTO livros (
                    titulo,
                    ano_publicacao,
                    id_autor,
                    id_editora,
                    id_categoria,
                    preco,
                    estoque
                )
                VALUES (
                    %s,
                    %s,
                    DEFAULT,
                    DEFAULT,
                    DEFAULT,
                    %s,
                    %s
                )
            """

            cursor.execute(query, (title, year, price, stock))
            self.conn.commit()

        except Exception as e:
            print("Erro ao inserir livro:", e)

        else:
            print("Livro inserido com sucesso")

