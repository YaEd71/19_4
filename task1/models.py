from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100) # для имени пользователя
    balance = models.DecimalField(max_digits=10, decimal_places=2) # для баланса с 10 цифрами всего и 2 после запятой
    age = models.PositiveIntegerField() #  для возраста (только положительные числа)

    def __str__(self):
        return f"{self.name} (Age: {self.age})"

class Game(models.Model):
    title = models.CharField(max_length=200) # для названия игры
    cost = models.DecimalField(max_digits=10, decimal_places=2) # для цены
    size = models.DecimalField(max_digits=10, decimal_places=2) # для размера файлов
    description = models.TextField() # для неограниченного описания
    age_limited = models.BooleanField(default=False) # для ограничения возраста, по умолчанию False
    buyer = models.ManyToManyField(Buyer, related_name='games') # для связи с моделью Buyer

    def __str__(self):
        return f"{self.title} (${self.cost})"
