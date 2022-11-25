import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='novobd', user = 'root', password = 'puabrasil206')

    inserir_produtos = """INSERT INTO banco_teste
                        (id_teste, nome_teste, data_teste)
                        VALUES
                        (4, 'gio', 12/12/1994),
                        (5, 'flavia', 15/12/1994),
                        (6, 'roberta', 18/12/1994)
                        """

    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registro insterido na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir: {}".format(erro))

finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("conexão finalizada.")