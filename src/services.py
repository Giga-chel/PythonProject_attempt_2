import re

def process_bank_search(data:list[dict], search:str)->list[dict]:
    result = []
    for item in data:
        description = item.get('description', '')
        if re.search(search, description, flags=re.IGNORECASE):
            result.append(item)
    return result


def process_bank_operations(data:list[dict], categories:list)->dict:
    result = {category: 0 for category in categories}
    for item in data:
        for category in categories:
            if re.search(category.lower(), item['description'], flags=re.IGNORECASE):
                result[category] += 1
    return result
