from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "stock", "rating"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price <= 0:
            raise ValidationError("Price must be a positive number")
        return price

    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        if stock < 0:
            raise ValidationError("Stock cannot be negative")
        return stock
