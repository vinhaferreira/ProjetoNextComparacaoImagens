from PIL import Image 
#Importando dependência
import imagehash
from receber_dados_bd import receber_dados_bd
import pandas

def comparacao_phash_2img(hash1, hash2):
    if (hash1 == hash2):
        print ("As imagens são iguais!")
    else:
        #Transformando a diferença entre as imgaens em string (quando estava em int, estava apresentando erro)
        diference = str(hash1-hash2)/64*100
        #Comparando as imagens para determinar se são iguais ou não:  
        print('As imagens são diferentes, a distância entre elas é de:' + diference + '%')  #hamming distance

def comparacao_phash_banco(hash1):
    df = receber_dados_bd()
    for i in df.itertuples():
        sim = 0
        diff = 0
        for j in range(0,len(hash1),1):
            if hash1[j] == i.phash[j]:
                sim = sim + 1
            else:
                diff = diff +1
        break
   
    

comparacao_phash_banco("asdasfasd")