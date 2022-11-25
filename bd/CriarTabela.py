import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", database="novobd",user = "root", password = "puabrasil206")

    criar_tabela_SQL = """CREATE TABLE nova_tabela (
                           IdProduto int(11) NOT NULL,
                           NomeProduto VARCHAR(70) NOT NULL,
                           Preco FLOAT NOT NULL,
                           Quantidade TINTINT NOT NULL,
                           Primary Key (IdProduto));"""

    cursor = con.cursor()
    cursor.execute(criar_tabela_SQL)
    print("Tabela criada com sucesso")
except mysql.connector.Error as erro:
    print("Falha ao criar tabela: ()".format(erro))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão finalizada.")