menu = {
    'pizza': 200,
    'pasta': 350,
    'burger': 200,
    'sandwich': 150,
    'cold coffee': 100,
    'hot coffee': 50,
    'cold drink': 50,
    'salad': 300
}
print("Welcome to the Cafe")
print("pizza: 200\npasta: 350\nburger: 200\nsandwich: 150\ncold coffee: 100\nhot coffee: 50\ncold drink: 50\nsalad: 300\n")

order_total = 0

item_1 = input("Enter the item you want to order:")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet")

another_item = input("Do you want to order another item? (yes/no): ")
if another_item.lower() == "yes":
    item_2 = input("Enter the item you want to order:")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet")

print(f"Your total order amount of items to pay: {order_total}")
