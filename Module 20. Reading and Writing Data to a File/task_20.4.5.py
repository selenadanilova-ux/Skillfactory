import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')


max_quantity = -1
best_order_id = None

for order_id, order_info in orders.items():
    if order_info['quantity'] > max_quantity:
        max_quantity = order_info['quantity']
        best_order_id = order_id

if best_order_id:
    print(f"Номер заказа с самым большим количеством товаров: {best_order_id} (количество: {max_quantity} шт.).")
else:
    print("Список заказов пуст.")


from collections import Counter

july_dates = [
    order_info['date']
    for order_info in orders.values()
    if order_info['date'].startswith('2023-07')
]

if july_dates:
    most_common_date, count = Counter(july_dates).most_common(1)[0]
    print(f"День в июле с наибольшим количеством заказов: {most_common_date} (всего {count} заказов).")
else:
    print("Заказы за июль не найдены.")


from collections import defaultdict

user_quantities_july = defaultdict(int)

for order_info in orders.values():
    if order_info['date'].startswith('2023-07'):
        user_quantities_july[order_info['user_id']] += order_info['quantity']

if user_quantities_july:
    best_user_id = max(user_quantities_july, key=user_quantities_july.get)
    max_quantity = user_quantities_july[best_user_id]
    print(f"Пользователь с ID {best_user_id} сделал наибольшее количество заказов (по количеству товаров) в июле: {max_quantity} шт.")
else:
    print("Заказы за июль не найдены.")


user_total_spent = defaultdict(int)

for order_info in orders.values():
    if order_info['date'].startswith('2023-07'):
        user_total_spent[order_info['user_id']] += order_info['price']

if user_total_spent:
    best_user_id = max(user_total_spent, key=user_total_spent.get)
    max_spent = user_total_spent[best_user_id]
    print(f"Пользователь с ID {best_user_id} имеет самую большую суммарную стоимость заказов в июле: {max_spent} руб.")
else:
    print("Заказы за июль не найдены.")


total_cost_july = 0
order_count_july = 0

for order_info in orders.values():
    if order_info['date'].startswith('2023-07'):
        total_cost_july += order_info['price']
        order_count_july += 1

if order_count_july > 0:
    average_cost = total_cost_july / order_count_july
    print(f"Средняя стоимость заказа в июле составила: {average_cost:.2f} руб.")
else:
    print("Заказы за июль не найдены.")


total_cost_july = 0
total_quantity_july = 0

for order_info in orders.values():
    if order_info['date'].startswith('2023-07'):
        total_cost_july += order_info['price']
        total_quantity_july += order_info['quantity']

if total_quantity_july > 0:
    average_item_cost = total_cost_july / total_quantity_july
    print(f"Средняя стоимость единицы товара в июле составила: {average_item_cost:.2f} руб.")
else:
    print("Товары за июль не найдены.")



