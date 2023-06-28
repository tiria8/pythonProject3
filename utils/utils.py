from datetime import datetime
import json

filename = '../operations.json'
def get_data(filename):
    """
    Получаем список транзакций
    :param file: JSON файл со списком операций, совершенных клиентом банка
    :return: список транзакций
    """
    with open(filename, "r", encoding='utf-8') as file:
        data = json.load(file)

    return data

def get_filtered_data(data):
    """
    Фильтрует транзакции по значению "state"=='EXECUTED'
    :param data: список транзакций
    :return: список транзакций со "state"=='EXECUTED'
    """
    filtered_data = []
    for i in data:
        if "state" in i and i["state"] == 'EXECUTED':
            filtered_data.append(i)

    return filtered_data

def get_last_transactions(data):
    """
    Фильтрует транзакции по дате и возвращает список последних 5 транзакций
    :param data: список транзакций
    :return:  список последних 5 транзакций, отсортированных по дате
    """

    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    sorted_data = sorted_data[:5]

    return sorted_data

def encrypted_transaction(bill_info):
    """
    Шифрует данные карты/счета
    :param bill_info: данные карты/счета
    :return: зашифрованные данные карты/счета
    """
    bill_info = bill_info.split()
    bill = bill_info[-1]
    info = bill_info[0]

    if len(bill) == 16:
        encrypted_bill = f"{bill[:7]}** **** {bill[-4:]}"
    else:
        encrypted_bill = f"** {bill[-4:]}"

    return f"{info} {encrypted_bill}"

def formatted_data(data):
    """
    Возвращет отформатированный список транзакций
    :param data: список транзакций
    :return: отформатированный список транзакций
    """
    formatted_data = []
    for i in data:
        date = datetime.strptime(i['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = i['description']
        to_transaction = encrypted_transaction(i["to"])
        transaction_amount = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}"

        if "from" in i:
            from_transaction = encrypted_transaction(i["from"])

            transaction_data = f"{date} {description}\n{from_transaction} -> {to_transaction}\n{transaction_amount}"

        transaction_data = f"{date} {description}\n{to_transaction}\n{transaction_amount}"

        formatted_data.append(transaction_data)

    return formatted_data

def show_data(data):
    """
    Отдельно выводит отформатированную информацию по каждой транзакции
    :param data: отформатированный список транзакций
    :return: информация о каждой транзакции из списка
    """
    for i in data:
        print(f"{i}\n")
