import mysql.connector
import os

def deletar_banco(uuid):
    conexao = mysql.connector.connect(host="localhost", database="dadosimagem",user = "root", password = "qfCSH5J6W&!&q")
    cursor = conexao.cursor()

    comando = f'delete from banco_imagem where uuid = "{uuid}"'
    cursor.execute(comando)
    conexao.commit()

    cursor.close()
    conexao.close()
    
def deletar(uuid):
    deletar_banco(uuid)
    caminho = os.path.join('static', 'uploads', uuid)
    if os.path.exists(caminho):
        try:
            os.remove(caminho)
            return "Imagem deletada com sucesso"
        except Exception as e:
            return f"Error ao deletar"

