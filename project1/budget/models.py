from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Budget(models.Model):
    CATAGORY_CHOICES = (
    ('A', 'Food'),
    ('B', 'Clothing'),
    ('C', 'Housing'),
    ('D', 'Education'),
    ('E', 'Entertainment'),
    ('F', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=20)
    catagory = models.CharField(max_length=8, choices=CATAGORY_CHOICES)
    projected = models.PositiveIntegerField()
    actual = models.PositiveIntegerField()
