import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        default=0.0, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
    )