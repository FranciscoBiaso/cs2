Car MCP Project - Resumo das Principais Funcionalidades

- Cadastro automático de carros fictícios no banco de dados (marca, modelo, ano, cor, motor, combustível, etc).
- Servidor TCP que recebe filtros de busca do cliente e retorna veículos compatíveis.
- Cliente interativo no terminal, onde o usuário conversa com um agente virtual para informar os filtros de busca.
- Testes automatizados para garantir a integridade das consultas e dos dados.

Como executar:

1. Instale as dependências:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

2. Popule o banco de dados:
   export PYTHONPATH=.
   python3 populate/populate_db.py

3. Inicie o servidor (em um terminal):
   export PYTHONPATH=.
   python3 server/server.py

4. Rode o cliente (em outro terminal):
   export PYTHONPATH=.
   python3 client/client.py

5. Para rodar os testes:
   export PYTHONPATH=.
   pytest