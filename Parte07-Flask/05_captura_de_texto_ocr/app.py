from flask import Flask, render_template, request, send_file
import easyocr

import io


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/textoExtraido", methods = ['POST'])
def extrair_texto():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada', 400
    imagem = request.files['imagem']
    if imagem.filename == '':
        return 'Nenhuma imagem selecionada', 400
    render = easyocr.Reader(['en','pt'], gpu=False)
    result = render.readtext(imagem.read())
    texto_extraido = ' '.join([res[1] for res in result])
    return render_template("extracao.html",texto=texto_extraido)

@app.route("/exportarTexto", methods = ['POST'])
def exportar_texto():
    if request.method == 'POST':
        texto = request.form.get("texto", "")
        arquivo_buffer = io.BytesIO(texto.encode('utf-8'))
        return send_file(
            arquivo_buffer,
            mimetype='text/plain',
            as_attachment=True,
            download_name='texto_extraido.txt'
        )
    return render_template("exportar_sucesso.html")


if __name__ == "__main__":
    app.run(debug=True)