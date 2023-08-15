from django import forms
from .models import Dish, Order, Purchase


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "price", "quantity"]


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["customer_name", "dishes", "status"]

#     def clean_dishes(self):
#         selected_dishes = self.cleaned_data["dishes"]
#         # Add your custom validation logic here to verify dish availability
#         return selected_dishes


class OrderForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    quantities = forms.IntegerField(min_value=1)  # Adjust the validation as needed

    class Meta:
        model = Purchase
        fields = ["customer_name", "dishes", "quantities"]
