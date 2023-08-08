def display_menu():
  if not dishes:
    print("No dishes have been added yet.")
    return
  print(f"{'ID':<5}{'Name':<10}{'Price':<10}{'Availablity':<15}")

  for dish in dishes:
    print(
      f"{dish['id']:<5}{dish['name']:<10}{dish['price']:<10}{dish['availability']:<10}"
    )


def add_dish(id, name, price, availability):
  new_dish = {
    "id": id,
    "name": name,
    "price": price,
    "availability": availability
  }

  dishes.append(new_dish)
  print(f"Dish {name} added successfully!")


def remove_dish(id):
  for dish in dishes:
    if dish["id"] == id:
      dishes.remove(dish)
      print(f"Dish with ID {id} removed successfully!")
      return

  print(f"No dish with ID {id} found!")


def update_availability(id, availability):
  for dish in dishes:
    if dish["id"] == id:
      dish["availability"] = availability
      print(f"Availability for dish with ID {id} updated successfully!")
      return

  print(f"No dish with ID {id} found!")


def sum_numbers(numbers):
  return sum(numbers)


def take_order(customer_name, dish_ids):
  global order_id

  ordered_dishes = []

  total_price = 0

  for id in dish_ids:
    dish_exists = False

    for dish in dishes:
      if dish["id"] == id:
        dish_exists = True
        if dish["availability"]:
          ordered_dishes.append(dish)
          total_price += dish["price"]
        else:
          print(f"Dish with ID {id} is not available.")

    if not dish_exists:
      print(f"No dish with ID {id} exists.")

  if ordered_dishes:
    order = {
      "order_id": order_id,
      "customer_name": customer_name,
      "ordered_dishes": ordered_dishes,
      "total_price": total_price,
      "status": "received"
    }
    orders.append(order)

    order_id += 1
    print(f"Order received! Thank you, {customer_name}.")
    print(f"Your total is: ${total_price:.2f}")
  else:
    print("No available dishes were found in your order.")


def update_order_status(order_id, new_status):
  for order in orders:
    if order["order_id"] == order_id:
      order["status"] = new_status
      print(f"Status for order with ID {order_id} updated successfully!")
      return

  print(f"No order with ID {order_id} found!")


def review_orders():
  if not orders:
    print("No orders have been placed yet.")
    return

  for order in orders:
    print(f"Order ID: {order['order_id']}")
    print(f"Customer Name: {order['customer_name']}")
    print("Ordered Dishes:")
    for dish in order["ordered_dishes"]:
      print(f"  - {dish['name']}")
    print(f"Total Price: ${order['total_price']}")
    print(f"Status: {order['status']}\n")


def filter_orders():
  status = input("Please enter the status to filter by: ")

  if not orders:
    print("No orders have been placed yet.")
    return

  order_exists = False

  for order in orders:
    if order["status"] == status:
      order_exists = True
      print(f"Order ID: {order['order_id']}")
      print(f"Customer Name: {order['customer_name']}")
      print("Ordered Dishes:")
      for dish in order["ordered_dishes"]:
        print(f"  - {dish['name']}")
      print(f"Total Price: ${order['total_price']}")
      print(f"Status: {order['status']}\n")

  if not order_exists:
    print(f"No orders with status '{status}' found.")

order_id = 1

orders = []

dishes = [
  {
    "id": 1,
    "name": "Pasta",
    "price": 12.99,
    "availability": True
  },
  {
    "id": 2,
    "name": "Burger",
    "price": 8.99,
    "availability": False
  },
  {
    "id": 3,
    "name": "Pizza",
    "price": 10.99,
    "availability": True
  },
  {
    "id": 4,
    "name": "Salad",
    "price": 7.99,
    "availability": True
  },
  {
    "id": 5,
    "name": "Soup",
    "price": 5.99,
    "availability": True
  },
  {
    "id": 6,
    "name": "Steak",
    "price": 15.99,
    "availability": True
  },
]

# Display menu options
print("Welcome to the Order Management System!")
print("Menu Options:")
print("1. Display the menu")
print("2. Add a dish")
print("3. Remove a dish")
print("4. Update availability of a dish")
print("5. Take an order")
print("6. Review orders")
print("7. Update order status")
print("8. Filter orders by status")
print("9. Exit")

while True:
  choice = input("\nPlease enter your choice (1-9): ")
  if choice == "1":
    display_menu()
  elif choice == "2":
    id = int(input("Enter the dish ID: "))
    name = input("Enter the dish name: ")
    price = float(input("Enter the dish price: "))
    availability = input(
      "Is the dish available? (True/False): ").lower() == "true"
    add_dish(id, name, price, availability)
  elif choice == "3":
    id = int(input("Enter the dish ID to remove: "))
    remove_dish(id)
  elif choice == "4":
    id = int(input("Enter the dish ID to update availability: "))
    availability = input(
      "Enter the new availability (True/False): ").lower() == "true"
    update_availability(id, availability)
  elif choice == "5":
    customer_name = input("Enter the customer name: ")
    dish_ids = list(
      map(int,
          input("Enter the dish IDs (separated by commas): ").split(",")))
    take_order(customer_name, dish_ids)
  elif choice == "6":
    review_orders()
  elif choice == "7":
    order_id = int(input("Enter the order ID to update status: "))
    new_status = input("Enter the new status: ")
    update_order_status(order_id, new_status)
  elif choice == "8":
    filter_orders()
  elif choice == "9":
    print("Exiting the system.")
    break
  else:
    print("Invalid option. Please enter a number between 1 and 9.")
