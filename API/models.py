from django.db import models

class Products(models.Model):
    item=models.CharField(max_length=200)
    price=models.CharField(max_length=50)
    def __str__(self):
        return self.item
