import mysql.connector
from mysql.connector import Error

def conectar_bd():

    con = mysql.connector.connect(host="localhost", database="bd",user = "root", password = "qfCSH5J6W&!&q")

    if con.is_connected() :
        db_info = con.get_server_info()
        print("Conectado no servidor versão", db_info)
        cursor = con.cursor()
        cursor.execute("select database();")
        linha = cursor.fetchone()
        print("Conectado ao banco de dados ", linha)

    return con

def fechar_bd(conexao, cursor):
    if conexao.is_connected() :
        cursor.close()
        conexao.close()
        print("Conexão encerrada")
        
def inserir_banco(nome, uuid, phash):
    var = "('" + nome + "','" + uuid + "','" + phash + "')"

    try:
        con = conectar_bd()

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
        fechar_bd(con, cursor)
