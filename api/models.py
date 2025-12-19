from django.db import models

# Create your models here.

class TV(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    model_number = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    screen_size = models.DecimalField(max_digits=5, decimal_places=2)  # inches
    resolution = models.CharField(max_length=50)  # e.g., '4K', 'Full HD'
    smart_tv = models.BooleanField(default=True)
    features = models.TextField(blank=True)  # comma-separated features
    stock = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model_number})"