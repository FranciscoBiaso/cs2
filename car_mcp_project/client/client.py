import socket
from utils.mcp_protocol import encode_message, decode_message

HOST = '127.0.0.1'
PORT = 9999

def collect_filters():
    print("Olá! Vou te ajudar a buscar um carro ideal :)")
    brand = input("Qual marca deseja? (ou deixe vazio) ")
    year = input("Ano específico? (ou deixe vazio) ")
    fuel = input("Tipo de combustível? (Gasolina, Etanol, Flex, Diesel, Elétrico, ou vazio) ")
    return {
        'brand': brand or None,
        'year': int(year) if year else None,
        'fuel': fuel or None
    }

def show_results(results):
    if not results:
        print("Nenhum veículo encontrado com os filtros aplicados.")
    else:
        print(f"Encontrei {len(results)} opções para você:\n")
        for car in results:
            print(f"{car['brand']} {car['model']} | Ano: {car['year']} | Cor: {car['color']} | Km: {car['mileage']} | R$ {car['price']:,.2f}")

def main():
    filters = collect_filters()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(encode_message(filters))
        data = b""
        while True:
            chunk = s.recv(4096)
            if not chunk: break
            data += chunk
            if b'\n' in chunk: break
        results = decode_message(data)
        show_results(results)

if __name__ == "__main__":
    main()
