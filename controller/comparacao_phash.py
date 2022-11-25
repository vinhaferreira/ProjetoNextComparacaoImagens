from PIL import Image 
#Importando dependência
import imagehash
#Criando número Hash da primeira imagem
hash = imagehash.phash(Image.open(r'C:\Users\Gustavo\Desktop\projetoNEXT\Phash\images/1.png'),hash_size= 10)
print ('Imagem 1: ' + str(hash))

#Criando número Hash da segunda imagem
otherhash = imagehash.phash(Image.open(r'C:\Users\Gustavo\Desktop\projetoNEXT\Phash\images/2.png'),hash_size= 10)
print('Imagem 2:' + str(otherhash))

#Transformando a diferença entre as imgaens em string (quando estava em int, estava apresentando erro)
diference = str(hash-otherhash)

#Comparando as imagens para determinar se são iguais ou não:  
if (hash == otherhash):
    print ("As imagens são iguais!")
else:
    print('As imagens são diferentes, a distância entre elas é de:' + diference)  #hamming distance
