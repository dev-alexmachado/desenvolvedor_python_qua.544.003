from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/textoExtraido")
def extrair_texto():
    return render_template("extracao.html")


if __name__ == "__main__":
    app.run(debug=True)