import json

def encode_message(data: dict) -> bytes:
    return (json.dumps(data) + '\n').encode()

def decode_message(data: bytes) -> dict:
    return json.loads(data.decode())
