from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API ativa e funcionando no Render!"})

@app.route('/processar-comando', methods=['POST'])
def processar_comando():
    data = request.json
    acao = data.get("acao")

    if acao == "gerar_relatorio":
        return jsonify({"status": "Relatório gerado no Looker Studio!"})

    elif acao == "atualizar_airtable":
        return jsonify({"status": "Dados atualizados no Airtable!"})

    return jsonify({"status": "Ação desconhecida!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
 
