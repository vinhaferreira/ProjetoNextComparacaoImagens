import mysql.connector

def deletar(uuid):
    conexao = mysql.connector.connect(host="localhost", database="dadosimagem",user = "root", password = "qfCSH5J6W&!&q")
    cursor = conexao.cursor()

    comando = f'delete from banco_imagem where uuid = "{uuid}"'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()

    

deletar("4f553228-306d-4127-8925-18301fcd045f.jpg")