from django.db import models
from django.conf import settings

# Create your models here.

class Recipe(models.Model):
    CategoryChoice = [
        ('Desert', 'Desert'),
        ('Main Course', 'Main Course'),
        ('Breakfast', 'Breakfast'),
        ('vegertrian', 'vegetrian'),
        ('appetizer', 'Appetizer'),
        ('drink', 'Drink'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    Title = models.CharField(max_length=200, blank=True, null=True)
    Description = models.TextField()
    Ingredients = models.TextField()
    Instructions = models.TextField(blank=True,null=True)
    Category = models.CharField(choices=CategoryChoice, max_length=100)
    Preparation_Time = models.PositiveIntegerField(help_text='Preparation time in minutes')
    Cooking_Time = models.PositiveIntegerField(help_text='Cooking time in minutes')
    Servings = models.PositiveIntegerField()
    Created_Date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"title: {self.Title}"
