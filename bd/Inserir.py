import mysql.connector
from mysql.connector import Error

nome = " ' teste ' "
uuid = " 'carlos' "
phash = " 'testando ' "
var = "(" + nome + "," + uuid + "," + phash + ")"

try:
    con = mysql.connector.connect(host='localhost',database='dadosimagem', user = 'root', password = 'puabrasil206')

    inserir_produtos = """INSERT INTO banco_imagem
                        (name_img, uuid, phash)
                        VALUES
                        """ + var

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