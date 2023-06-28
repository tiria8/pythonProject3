import pytest

@pytest.fixture
def test_data():
    return [
        {'id': 863064926, 'state': 'CANCELLED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
        {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'},
        {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
        {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
        {'id': 185048835, 'state': 'EXECUTED', 'date': '2019-05-06T00:17:42.736209', 'operationAmount': {'amount': '74895.83', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 27921306202254867520', 'to': 'Счет 49884962711830774470'},
        {'id': 422035015, 'state': 'EXECUTED', 'date': '2019-02-27T03:59:25.921176', 'operationAmount': {'amount': '69311.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'MasterCard 8847384717023026', 'to': 'Счет 85458008326755993377'},
        {'id': 917824439, 'state': 'EXECUTED', 'date': '2019-07-18T12:27:13.355343', 'operationAmount': {'amount': '82139.20', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Platinum 6942697754917688', 'to': 'МИР 2956603572573342'}
    ]

@pytest.fixture
def test_data_filtered():
    return [{'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
            {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}
    ]
