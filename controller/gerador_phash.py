from PIL import Image
import imagehash

def gerador_phash(filename):
    # Create the Hash Object of the first image
    codigo_hash = str(imagehash.phash(Image.open('./uploads/'+filename)))
    return codigo_hash
