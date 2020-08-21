from flask import Flask  # nosso app
from flask import request  # recebe as informações do usuário
from flask import jsonify  # transforma dicionários em json
from flask import render_template  # carrega a página web
import os

from functions import mainFunction  # sua logica

app = Flask(__name__)


@app.route('/results', methods=["POST"])
def resultado():
    resp = request.form  # pega informações do usuário
    result = mainFunction(resp)  # usa informações para calcular resultado
    # retorna resultado para usuário
    return render_template("results.html", result=result)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
