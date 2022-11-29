from PIL import Image 
#Importando dependência
import imagehash
# from receber_dados_bd import receber_dados_bd
import pandas as pd
from IPython.display import display
import mysql.connector
from mysql.connector import Error

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

def receber_dados_bd():
    con = mysql.connector.connect(host='localhost',database='dadosimagem', user = 'root', password = 'qfCSH5J6W&!&q')
    q1 = """
    SELECT *
    FROM banco_imagem;
    """
    results = read_query(con, q1)

    # Retorna uma lista de listas e cria um DataFrame do Pandas
    from_db = []

    for result in results:
        result = list(result)
        from_db.append(result)

    #print(from_db)


    columns = ["nome", "uuid", "phash"]
    df = pd.DataFrame(from_db, columns=columns)
    #for result in results:
    # print(result)

    # display(df)
    return df

def comparacao_phash_2img(hash1, hash2):
    restored_hash1 = imagehash.hex_to_hash(hash1)
    restored_hash2 = imagehash.hex_to_hash(hash2)

    if (restored_hash1 == restored_hash2):
        #print ("As imagens são iguais!")
        return 0
    else:
        #Transformando a diferença entre as imgaens em string (quando estava em int, estava apresentando erro)
        diference = int(restored_hash1-restored_hash2)/64*100
        #print(diference)
        #Comparando as imagens para determinar se são iguais ou não:  
        #print('As imagens são diferentes, a distância entre elas é de:' + diference + '%')  #hamming distance
        return diference

def comparacao_phash_banco(hash1):
    df = receber_dados_bd()
    maior_porc = 100
    for i in df.itertuples():
        hash2 = i.phash
        dif = comparacao_phash_2img(hash1,hash2)
        #print('Código UUID:'+ str(i.uuid) + ' diferença: ' + str(dif) + '%')
        if dif < maior_porc:
            maior_porc = dif
            img_mais_similar = i.uuid
    return [img_mais_similar, maior_porc]
   
    
#comparacao_phash_2img("ffd3c181818181ff", "e3c38787878d8f81")
    
# img = comparacao_phash_banco("c86817d80cb76cb7")

# print('A imagem mais similar é :' , img)