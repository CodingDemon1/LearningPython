from django.shortcuts import render, redirect
from .models import Dish, Order, Purchase, OrderDetail
from .forms import DishForm, OrderForm
from django.urls import reverse
from decimal import Decimal

# Create your views here.


def menu(request):
    dishes = Dish.objects.all()
    return render(request, "menu.html", {"dishes": dishes})


def order(request):
    if request.method == "POST":
        # Process the order and update database
        return render(request, "order_confirmation.html")

    dishes = Dish.objects.all()
    return render(request, "order.html", {"dishes": dishes})


# def add_dish(request):
#     if request.method == "POST":
#         form = DishForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("menu")
#     else:
#         form = DishForm()

#     return render(request, "add_dish.html", {"form": form})


def add_dish(request):
    if request.method == "POST":
        dish_form = DishForm(request.POST)
        if dish_form.is_valid():
            dish = dish_form.save(commit=False)
            if dish.quantity > 0:
                dish.status = True  # Dish is available
            else:
                dish.status = False  # Dish is not available
            dish.save()
            return redirect("menu")  # Redirect to the menu page after adding the dish
    else:
        dish_form = DishForm()
    return render(request, "add_dish.html", {"dish_form": dish_form})


def order_confirmation(request):  # Add the order_id parameter
    return render(request, "order_confirmation.html")


# def place_order(request):
#     if request.method == "POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             customer_name = order_form.cleaned_data["customer_name"]
#             selected_dishes = order_form.cleaned_data["dishes"]
#             total_quantity = order_form.cleaned_data["quantities"]
#             print(customer_name, selected_dishes, total_quantity)

#             for dish in selected_dishes:
#                 quantity = (
#                     total_quantity  # Set the same quantity for all selected dishes
#                 )
#                 if dish.quantity >= quantity:
#                     dish.quantity -= quantity
#                     dish.save()
#                     Purchase.objects.create(
#                         customer_name=customer_name, dish=dish, quantity=quantity
#                     )
#             return redirect(
#                 "order_confirmation"
#             )  # Redirect to the order confirmation page after placing the order
#     else:
#         order_form = OrderForm()
#     return render(request, "place_order.html", {"order_form": order_form})


# def place_order(request):
#     if request.method == "POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             customer_name = order_form.cleaned_data["customer_name"]
#             selected_dishes = order_form.cleaned_data["dishes"]

#             order = Order.objects.create(customer_name=customer_name)

#             for dish in selected_dishes:
#                 OrderDetail.objects.create(
#                     order=order, dish=dish, quantity=1
#                 )  # You can adjust quantity as needed

#             return redirect("order_confirmation", order_id=order.id)
#     else:
#         order_form = OrderForm()


#     return render(request, "place_order.html", {"order_form": order_form})
# from .models import OrderDetail  # Import the OrderDetail model
# def place_order(request):
#     if request.method == "POST":
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             customer_name = order_form.cleaned_data["customer_name"]
#             selected_dishes = order_form.cleaned_data["dishes"]

#             purchase_data = []
#             total_price = 0

#             for dish in selected_dishes:
#                 dish_data = {
#                     "name": dish.name,
#                     "price": dish.price,
#                     "quantity": 1,  # You can modify this as needed
#                 }
#                 purchase_data.append(dish_data)
#                 total_price += dish.price

#             purchase = Purchase.objects.create(
#                 customer_name=customer_name,
#                 selected_items=purchase_data,
#                 total_price=total_price,
#             )

#             return redirect("order_confirmation", purchase_id=purchase.id)
#     else:
#         order_form = OrderForm()

#     return render(request, "place_order.html", {"order_form": order_form})


def place_order(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            customer_name = order_form.cleaned_data["customer_name"]
            selected_dishes = order_form.cleaned_data["dishes"]
            total_quantity = order_form.cleaned_data["quantities"]

            for dish in selected_dishes:
                quantity = (
                    total_quantity  # Set the same quantity for all selected dishes
                )
                if dish.quantity >= quantity:
                    dish.quantity -= quantity
                    dish.save()
                    Purchase.objects.create(
                        customer_name=customer_name, dish=dish, quantity=quantity
                    )
            return redirect(
                "order_confirmation"
            )  # Redirect to the order confirmation page after placing the order
    else:
        order_form = OrderForm()
    return render(request, "place_order.html", {"order_form": order_form})


def update_order_status(request, order_id):
    order = Order.objects.get(pk=order_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        order.status = new_status
        order.save()
        return redirect("order_confirmation")

    return render(request, "update_order_status.html", {"order": order})


def view_orders(request):
    orders = Purchase.objects.all()

    return render(request, "view_orders.html", {"orders": orders})


def update_menu(request):
    dishes = Dish.objects.all()
    dish_forms = []

    if request.method == "POST":
        for dish in dishes:
            form = DishForm(
                request.POST, instance=dish, prefix=dish.id
            )  # Use the dish id as a prefix for each form
            dish_forms.append(form)
            if form.is_valid():
                form.save()
            else:
                # Handle form errors if needed
                pass
        return redirect("menu")  # Redirect back to the menu after updating
    else:
        for dish in dishes:
            form = DishForm(
                instance=dish, prefix=dish.id
            )  # Use the dish id as a prefix for each form
            dish_forms.append(form)

    return render(request, "update_menu.html", {"dish_forms": dish_forms})
