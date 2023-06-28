from utils.utils import get_data, get_filtered_data, get_last_transactions, formatted_data, show_data

data = get_data()
filtered_data = get_filtered_data(data)
last_transactions = get_last_transactions(filtered_data)
formatted_data = formatted_data(last_transactions)
final_data = show_data(formatted_data)

print(final_data)
