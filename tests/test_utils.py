from tests.conftest import test_data
from utils.utils import get_data, get_filtered_data, get_last_transactions, encrypted_transaction, formatted_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_filtered_data(test_data):
    data = get_filtered_data(test_data)
    assert len(data) == 6

def test_get_last_transactions(test_data):
    data = get_last_transactions(test_data)
    assert [x['date'] for x in data] == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-05T12:04:13.781725', '2019-07-18T12:27:13.355343']

def test_encrypted_transaction():
    assert encrypted_transaction('Maestro 7810846596785568') == 'Maestro 7810846** **** 5568'
    assert encrypted_transaction('Счет 77613226829885488381') == 'Счет ** 8381'

def test_formatted_data(test_data_filtered):
   assert formatted_data(test_data_filtered) == ['05.11.2019 Открытие вклада\nСчет ** 8381\n21344.35 руб.', '07.12.2019 Перевод организации\nСчет ** 3655\n48150.39 USD']








