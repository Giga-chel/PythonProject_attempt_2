def filter_by_currency(transactions, currency_code):
    for item in transactions:
        if item['operationAmount']['currency']['code'] == currency_code:
            yield item

def transaction_descriptions(transactions):
    for item in transactions:
        yield item['description']

def card_number_generator(start, end):
    for num in range(start, end + 1):
        num_str = str(num)
        zeros_need = 16 - len(num_str)
        card_num = "0" * zeros_need + num_str
        first = card_num[0:4]
        second = card_num[4:8]
        third = card_num[8:12]
        fourth = card_num[12:16]
        full_card_num =' '.join([first, second, third, fourth])
        yield full_card_num
