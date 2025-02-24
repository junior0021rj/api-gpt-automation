from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Chave de autenticação para segurança
API_SECRET = os.getenv("API_SECRET", "seu_token_secreto")

@app.before_request
def autenticar():
    """Verifica se a requisição possui a chave de autenticação correta"""
    token = request.headers.get("Authorization")
    if token != f"Bearer {API_SECRET}":
        return jsonify({"erro": "Acesso não autorizado"}), 403

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API ativa e funcionando no Render!"})

@app.route('/healthz', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route('/processar-comando', methods=['POST'])
def processar_comando():
    """Processa comandos recebidos na API"""
    data = request.json
    acao = data.get("acao")

    if acao == "gerar_relatorio":
        return jsonify({"status": "Relatório gerado no Looker Studio!"})

    elif acao == "atualizar_banco":
        return atualizar_google_sheets()

    elif acao == "buscar_tendencias":
        return buscar_tendencias_google()

    return jsonify({"status": "Ação desconhecida!"})

def atualizar_google_sheets():
    """Função para atualizar o Google Sheets"""
    return jsonify({"status": "Dados atualizados no Google Sheets!"})

def buscar_tendencias_google():
    """Consulta tendências no Google Trends"""
    return jsonify({"status": "Tendências buscadas com sucesso!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
