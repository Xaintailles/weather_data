import json

secret_path = './secrets/secrets.json'

def fetch_secret(secret_name: str) -> str:
    with open(secret_path, 'r') as file:
        data = json.load(file)

    return data[secret_name]