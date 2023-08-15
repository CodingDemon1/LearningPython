from django.db import models
from django.utils import timezone

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = (
        ("received", "Received"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    )

    customer_name = models.CharField(max_length=100)
    dishes = models.ManyToManyField(Dish)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="received")

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


# class Purchase(models.Model):
#     customer_name = models.CharField(max_length=100)
#     selected_items = models.JSONField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.customer_name}'s Purchase"


#     def update_total_price(self):
#         self.total_price = sum(
#             item["quantity"] * item["dish"].price for item in self.selected_items
#         )
#         self.save()
# class Purchase(models.Model):
#     customer_name = models.CharField(max_length=100)
#     dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.customer_name} purchased {self.quantity} of {self.dish.name}"


# class Purchase(models.Model):
#     customer_name = models.CharField(max_length=100)
#     selected_items = models.JSONField()
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f"{self.customer_name}'s Purchase"


#     def update_total_price(self):
#         self.total_price = sum(
#             item["quantity"] * item["dish"].price for item in self.selected_items
#         )
#         self.save()
class Purchase(models.Model):
    customer_name = models.CharField(max_length=100)
    selected_items = models.JSONField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.customer_name}'s Purchase"

    def update_total_price(self):
        self.total_price = sum(
            item["quantity"] * item["dish"].price for item in self.selected_items
        )
        self.save()


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.purchase.total_price += self.dish.price * self.quantity
        self.purchase.save()
        super(PurchaseItem, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.purchase.total_price -= self.dish.price * self.quantity
        self.purchase.save()
        super(PurchaseItem, self).delete(*args, **kwargs)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1
    )  # You can set a default value here

    def __str__(self):
        return f"{self.order.customer_name} - {self.dish.name}"
