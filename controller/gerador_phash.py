from PIL import Image 
#Importando dependência
import imagehash
#Criando número Hash da primeira imagem

def gerador_phash(filename):
    # Create the Hash Object of the first image
    codigo_hash = str(imagehash.phash(Image.open(r'./static/uploads/'+filename), hash_size= 8))
    return codigo_hash

def gerador_phash_temp(filename):
    # Create the Hash Object of the first image
    codigo_hash = str(imagehash.phash(Image.open(r'./static/temp/'+filename), hash_size= 8))
    return codigo_hash


