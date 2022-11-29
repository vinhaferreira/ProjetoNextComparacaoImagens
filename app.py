import os
import urllib.request
from controller.renomearimagem import renomearimagem
from controller.gerador_phash import gerador_phash, gerador_phash_temp
from bd.Inserir import inserir_banco
from bd.deletar_banco import deletar
from controller.comparacao_phash import comparacao_phash_banco, comparacao_phash_2img
from flask import Flask, flash, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

#inicializa o flask
app = Flask(__name__, template_folder='./view/templates',static_folder='static')

#diretorio onde serão salvas as imagens
UPLOAD_FOLDER = os.path.join('static', 'uploads')
TEMP_FOLDER = os.path.join('static', 'temp')

app.secret_key = "projetonextt3"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TEMP_FOLDER'] = TEMP_FOLDER
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
            #salva o nome do original arquivo no vetor
            filename = secure_filename(file.filename)
            file_names.append(filename)
            #salva a imagem
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            try:
                gerador_phash(filename)
                #renomeia o arquivo
                fileuuid = renomearimagem(filename)
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
        
    return render_template('upload.html', filenames = file_uuid)

@app.route('/display/<filename>')
def display_image(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = '/uploads/' + filename), code = 301)


@app.route("/deletar")
def deletar_img():
    return render_template('delete.html')

@app.route("/deletar", methods = ['POST'])
def deletar_imagem():
    filename = request.form.get('uuid')
    print(request.form.get('uuid'))
    try:
        deletar(filename+'.jpg')
        flash("Imagem deletada com sucesso")
    except:
        flash("Erro ao deletar")
    return render_template('delete.html')


@app.route("/comparacao")
def comparacao_form():
    return render_template('comparacao1.html')

@app.route("/comparacao", methods = ['POST'])
def comparacao_imagem():
    
    if 'arquivo' not in request.files:
        flash('Nenhum arquivo encontrado')
        
    file = request.files.get('arquivo')
    
  
    if file and allowed_file(file.filename):
            #salva o nome do arquivo no vetor
            filename = secure_filename(file.filename)
            #salva a imagem
            file.save(os.path.join('./static/temp/', filename))
            try:
                phash_temp = str(gerador_phash_temp(filename))
                dados = comparacao_phash_banco(phash_temp)
                uuid = dados[0]
                nome_original = dados[2]
                diferenca = dados[1]
                if diferenca == 0:
                    flash("A imagem " + nome_original + " é igual à selecionada.")
                else:
                    flash("A imagem " + nome_original + " é a mais similar à selecionada.")
                    flash("A diferença é de "+ str(diferenca)+ "%")
                os.remove(os.path.join('static', 'temp', filename))
            except:
                flash("Erro na comparação")
                return redirect('/comparacao')
    else:
        flash('Só são permitidas imagens com extensão .jpg.')
        return redirect('/comparacao')
    
    return render_template('comparacao1.html', filename = uuid)

@app.route('/comparacao/display/<filename>')
def display_image_comp(filename):
    print('display_image filename: ' + filename)
    return redirect(url_for('static', filename = '/uploads/' + filename), code = 301)


@app.route("/comparacao2")
def comparacao_form2():
    return render_template('comparacao2.html')

@app.route("/comparacao2", methods = ['POST'])
def comparacao2_imagem():

    if 'files[]' not in request.files:
        flash('Nenhum arquivo encontrado')
        
    files = request.files.getlist('files[]')
    phash_temp = []
    print(len(files))

    if len(files)==2:
        for file in files:
            if file and allowed_file(file.filename):
                    #salva o nome do arquivo no vetor
                    filename = secure_filename(file.filename)
                    #salva a imagem
                    file.save(os.path.join('./static/temp/', filename))
                    try:
                        phash = str(gerador_phash_temp(filename))
                        phash_temp.append(phash)
                        os.remove(os.path.join('./static/temp/', filename))
                    except:
                        flash("Erro ao gerar o hash")
                        return redirect('/comparacao2')
            else:
                flash('Só são permitidas imagens com extensão .jpg.')
                return redirect('/comparacao2')
        dif = comparacao_phash_2img(phash_temp[0], phash_temp[1])

        if dif == 0:
            flash("As imagens são iguais.")
        else:
            flash("A diferença entre as imagens é de " + str(dif) + "%.")

    else:
        flash('Só é permitido o upload de 2 imagens.')
        return redirect('/comparacao2')
    return render_template('comparacao2.html')

if __name__ == "__main__":
    app.run(debug=True)