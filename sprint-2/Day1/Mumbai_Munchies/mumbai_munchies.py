def initialize_inventory():
  inventory = {
    1: {
      "name": "Samosa",
      "price": 10,
      "available": True,
      "quantity": 20
    },
    2: {
      "name": "Pakora",
      "price": 15,
      "available": False,
      "quantity": 0
    },
    3: {
      "name": "Gulab Jamun",
      "price": 40,
      "available": True,
      "quantity": 10
    }
  }
  return inventory


def display_inventory(inventory):
  print("\nMenu:")
  print(f"{'ID':<5}{'Name':<15}{'Price':<10}{'Quantity':<10}{'Available':<10}")
  for id, snack in inventory.items():
    print(
      f"{id:<5}{snack['name']:<15}{snack['price']:<10}{snack['quantity']:<10}{str(snack['available']):<10}"
    )


def add_snack(inventory):
  snack_id = int(input("Enter snack ID: "))
  snack_name = input("Enter snack name: ")
  price = int(input("Enter price: "))
  quantity = int(input("Enter quantity: "))

  if snack_id in inventory:
    print("\nSnack ID already exists in the inventory!")
  else:
    inventory[snack_id] = {
      "name": snack_name,
      "price": price,
      "available": quantity > 0,
      "quantity": quantity
    }
    print("\nSnacks Added Successfully")
  return inventory


def remove_snack(inventory):
  snack_id = int(input("Enter snack ID to remove: "))

  if snack_id in inventory:
    del inventory[snack_id]
    print("\nSnacks removed ")
  else:
    print('Snack ID not found in the inventory!')
  return inventory


def update_quantity(inventory):
  snack_id = int(input("Enter snack ID: "))
  new_quantity = int(input("Enter new quantity: "))

  if snack_id in inventory:
    inventory[snack_id]['quantity'] = new_quantity
    inventory[snack_id]['available'] = new_quantity > 0
    print("\nQuantity updated")
  else:
    print("Snack ID not found in the inventory!")
  return inventory


def record_sale(inventory, sales):
  snack_id = int(input("Enter snack ID: "))
  sale_quantity = int(input("Enter sale quantity: "))

  if snack_id in inventory:
    if inventory[snack_id]['available'] and inventory[snack_id][
        'quantity'] >= sale_quantity:
      inventory[snack_id]['quantity'] -= sale_quantity
      inventory[snack_id]['available'] = inventory[snack_id]['quantity'] > 0

      if snack_id in sales:
        sales[snack_id] += sale_quantity
      else:
        sales[snack_id] = sale_quantity
      print("\nSales record updated")
    else:
      print("The snack is not available in the required quantity!")
  else:
    print("Snack ID not found in the inventory!")
  return inventory, sales


def display_sales(sales):
  print("Sales:")
  for snack_id, quantity in sales.items():
    print(f"Snack ID: {snack_id}, Quantity Sold: {quantity}")


def mumbai_munchies():
  inventory = initialize_inventory()
  sales = {}
  # print(inventory)
  while True:
    print("\nPlease select an operation:")
    print("1. Display the snacks")
    print("2. Add a snack")
    print("3. Remove a snack")
    print("4. Update snack quantity")
    print("5. Record a sale")
    print("6. Display sales")
    print("7. Exit")

    operation = int(input("\nEnter your selection (1-7): "))
    if operation == 1:
      display_inventory(inventory)
    if operation == 2:
      inventory = add_snack(inventory)
      display_inventory(inventory)
    elif operation == 3:
      inventory = remove_snack(inventory)
      display_inventory(inventory)
    elif operation == 4:
      inventory = update_quantity(inventory)
      display_inventory(inventory)
    elif operation == 5:
      inventory, sales = record_sale(inventory, sales)
      display_inventory(inventory)
    elif operation == 6:
      display_sales(sales)
    elif operation == 7:
      print("Have a nice day")
      break


mumbai_munchies()
