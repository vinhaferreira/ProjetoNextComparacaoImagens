from PIL import Image 
#Importando dependência
import imagehash
from receber_dados_bd import receber_dados_bd
import pandas

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
    return img_mais_similar
   
    
#comparacao_phash_2img("ffd3c181818181ff", "e3c38787878d8f81")
    
img = comparacao_phash_banco("c86817d80cb76cb7")

print('A imagem mais similar é :' , img)