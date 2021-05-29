from django.db import models

# Create your models here.

class Foo(models.Model):
    amount = models.DecimalField(
        null=False,
        decimal_places=18,
        max_digits=44)
