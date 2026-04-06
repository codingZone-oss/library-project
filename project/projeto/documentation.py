from class_conextion import cursor

def select_readers(value) -> None:

    query = (f' select id, nome, email, telefone, nacionality, city, number_identity, library_card_ticket from leitores where nome like "%{value}%"')

    try:
        cursor.execute(query)
    except Exception as e:
        print(f"ERROR EXECUTE QUERY: {e}"); return False
    else:
        return cursor.fetchall(); True

teste = select_readers("dfdnkdkfd")
if not teste:
    print(type(teste))
    print("vazio!")   
else:
    for c in teste:
        print(c)
    print(type(teste))
    print("cheio")