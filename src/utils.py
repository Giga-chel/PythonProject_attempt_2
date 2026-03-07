import json

def financial_transactions(file_path: str) -> list:
    try:
        with open(file_path) as json_file:
            data = json.load(json_file)
    except json.decoder.JSONDecodeError:
        data = []
    except FileNotFoundError:
        data = []
    if not isinstance(data, list):
        data = []
    return data