import uuid
import os

def renomear_imagem(nome_original):
    UPLOAD_FOLDER = './uploads/'
    codigo_uuid = str(uuid.uuid4())+'.jpg'

    os.rename(UPLOAD_FOLDER+nome_original, UPLOAD_FOLDER+codigo_uuid)