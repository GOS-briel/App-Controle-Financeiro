from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def health_check():
    """Endpoint simples pra confirmar que a API está de pé."""
    return jsonify({"status": "ok", "app": "controle-financeiro"})


if __name__ == "__main__":
    app.run(debug=True)


# Próximos endpoints (ainda não implementados):
# - GET  /lancamentos          -> listar lançamentos
# - POST /lancamentos          -> criar lançamento manual
# - GET  /categorias           -> listar categorias e tetos
# - PUT  /categorias/<id>      -> editar teto de categoria
# - POST /fatura/importar      -> upload de PDF Bradesco
