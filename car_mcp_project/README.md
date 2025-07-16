# Car MCP Project

## Requisitos

- Python 3.10+
- (Opcional) virtualenv

## Instalação

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Como rodar

1. Popule o banco:
   ```bash
   python3 populate/populate_db.py
   ```

2. Inicie o servidor:
   ```bash
   python3 server/server.py
   ```

3. Em outro terminal, rode o cliente:
   ```bash
   python3 client/client.py
   ```

4. Para rodar os testes:
   ```bash
   pytest
   ```
