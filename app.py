import os
import urllib.request
from controller.renomearimagem import renomearimagem
from controller.gerador_phash import gerador_phash
from bd.Inserir import inserir_banco
from bd.deletar_banco import deletar
from controller.comparacao_phash import comparacao_phash_banco
from controller.receber_dados_bd import receber_dados_bd

from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

#inicializa o flask
app = Flask(__name__, template_folder='./view/templates',static_folder='static')

#diretorio onde serão salvas as imagens
UPLOAD_FOLDER = os.path.join('static', 'uploads')
UPLOAD_FOLDER2 = os.path.join('static', 'temp')

app.secret_key = "projetonextt3"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    
@app.route("/")
def upload_form():
    return render_template('upload.html')


@app.route("/", methods = ['POST'])
def upload_image():
    
    if 'files[]' not in request.files:
        flash('Nenhum arquivo encontrado')
        
    files = request.files.getlist('files[]')
    file_names =[]
    file_uuid =[]
    file_phash = []

    for file in files:
        
        if file and allowed_file(file.filename):
            #salva o nome do arquivo no vetor
            filename = secure_filename(file.filename)
            file_names.append(filename)
            #salva a imagem
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                gerador_phash(filename)
                #renomeia o arquivo
                fileuuid = renomearimagem(filename)
                #salva o código uuid dessa imagem
                file_uuid.append(fileuuid)
                #gera o código p_hash
                filephash = gerador_phash(fileuuid)
                file_phash.append(filephash)
                inserir_banco(filename, fileuuid, filephash)
            except:
                flash("Imagem Corrompida")
                return redirect(request.url)

        else:
            flash('Só são permitidas imagens com extensão .jpg.')
            return redirect(request.url)
        
    return render_template('upload.html', filenames = file_names)

@app.route('/display/<filename>')
def display_image(filename):
    #print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = '/static/uploads/' + filename), code = 301)


@app.route("/deletar/<uuid>")
def deletar_a_imagem(uuid):
    filename = f"{uuid}.jpg"
    deletar(filename)
    return redirect('/deletar')

    
@app.route("/comparacao")
def comparacao_form():
    return render_template('comparacao.html')

@app.route("/comparacao", methods = ['POST'])
def comparacao_image():
    
    if 'arquivo' not in request.files:
        flash('Nenhum arquivo encontrado')
        
    file = request.files.getlist('arquivo')
    
  
    if file and allowed_file(file.filename):
            #salva o nome do arquivo no vetor
            filename = secure_filename(file.filename)
            #salva a imagem
            file.save(os.path.join(app.config['UPLOAD_FOLDER2'], filename))
            try:
                phash_temp = str(gerador_phash(filename))
                #renomeia o arquivo
                img_mais_parecida = comparacao_phash_banco(phash_temp)
            except:
                flash(img_mais_parecida)
                return redirect(request.url)

    else:
        flash('Só são permitidas imagens com extensão .jpg.')
        return redirect(request.url)
        
    return render_template('comparacao.html')


if __name__ == "__main__":
    app.run(debug=True)