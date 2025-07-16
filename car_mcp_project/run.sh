#!/bin/bash
set -e

source .venv/bin/activate
export PYTHONPATH=.

echo "Criando ambiente virtual..."
python3 -m venv .venv
source .venv/bin/activate
export PYTHONPATH=.

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Populando o banco de dados..."
python3 populate/populate_db.py

echo "Inicie o servidor MCP (em outro terminal):"
echo "  source .venv/bin/activate && python3 server/server.py"
echo "Depois, rode o cliente:"
echo "  source .venv/bin/activate && python3 client/client.py"

echo "Para rodar testes automatizados:"
echo "  pytest"
