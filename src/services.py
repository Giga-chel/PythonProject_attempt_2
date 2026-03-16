import re

def process_bank_search(data:list[dict], search:str)->list[dict]:
    result = []
    for item in data:
        description = item.get('description', '')
        if re.search(search, description, flags=re.IGNORECASE):
            result.append(item)
    return result

