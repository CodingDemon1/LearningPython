from django.urls import path
from . import views

urlpatterns = [
    path("menu/", views.menu, name="menu"),
    path("add_dish/", views.add_dish, name="add_dish"),
    path("place_order/", views.place_order, name="place_order"),
    path(
        "update_order/<int:order_id>/",
        views.update_order_status,
        name="update_order_status",
    ),
    path(
        "order_confirmation/<int:order_id>/",
        views.order_confirmation,
        name="order_confirmation",
    ),
    path("order_confirmation/", views.order_confirmation, name="order_confirmation"),
    path("view_orders/", views.view_orders, name="view_orders"),
    path("update_menu/", views.update_menu, name="update_menu"),
    # ... other URL patterns ...
]
