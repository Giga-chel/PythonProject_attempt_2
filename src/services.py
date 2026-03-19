import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    result = []
    for item in data:
        description = item.get("description", "")
        if re.search(search, description, flags=re.IGNORECASE):
            result.append(item)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    counts: Counter[str] = Counter()

    for item in data:
        description = item.get("description", "")
        for category in categories:
            if re.search(category.lower(), description, flags=re.IGNORECASE):
                counts[category] += 1

    result = {category: counts.get(category, 0) for category in categories}
    return result
