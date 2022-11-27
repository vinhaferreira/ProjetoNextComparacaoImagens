import mysql.connector
from mysql.connector import Error
import pandas as pd
from IPython.display import display

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

    #display(df)
    return df
    