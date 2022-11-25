from PIL import Image 
#Importando dependência
import imagehash
#Criando número Hash da primeira imagem

def gerador_phash(filename):
    # Create the Hash Object of the first image
    codigo_hash = str(imagehash.phash(Image.open(r'./uploads/'+filename), hash_size= 20))
    return codigo_hash


