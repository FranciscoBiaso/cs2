import socket
from db.models import get_engine, Car
from sqlalchemy.orm import sessionmaker
from utils.mcp_protocol import decode_message, encode_message

HOST = '127.0.0.1'
PORT = 9999

def query_cars(filters):
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(Car)
    for key, value in filters.items():
        if hasattr(Car, key) and value:
            query = query.filter(getattr(Car, key) == value)
    results = query.limit(20).all()
    return [
        {
            'brand': car.brand,
            'model': car.model,
            'year': car.year,
            'engine': car.engine,
            'fuel': car.fuel,
            'color': car.color,
            'mileage': car.mileage,
            'doors': car.doors,
            'transmission': car.transmission,
            'price': car.price,
        }
        for car in results
    ]

def main():
    print(f"Servidor MCP escutando em {HOST}:{PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = b""
                while True:
                    chunk = conn.recv(4096)
                    if not chunk: break
                    data += chunk
                    if b'\n' in chunk: break
                filters = decode_message(data)
                results = query_cars(filters)
                conn.sendall(encode_message(results))

if __name__ == "__main__":
    main()
