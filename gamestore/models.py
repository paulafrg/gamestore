from django.db import models
from django.core.exceptions import ValidationError

class Games(models.Model):
    CATEGORYS = (
        ('FPS', 'FPS'),
        ('MOBA', 'MOBA'),
        ('Strategy', 'Strategy'),
        ('RPG', 'RPF'),
        ('Others', 'Others'),
    )

    RATINGS = (
        ('PG', 'PG'),
        ('+14', '+14'),
        ('+16', '+16'),
        ('M', 'M'),
    )

    game = models.CharField(max_length=150, blank=False, null=False,)
    genre = models.CharField(max_length=10, choices=CATEGORYS, blank=False, null=False)
    rating = models.CharField(max_length=3, choices=RATINGS, blank=False, null=False)
    quantity = models.PositiveIntegerField(max_length=3, blank=False, null=False, default=1)

    def __str__(self):
        return self.game
    
class Customers(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    dob = models.DateField(default='%m/%d/%Y', blank=False, null=False)

    def __str__(self):
        return self.name

class Rents(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(max_length=3, blank=False, null=False, default=1)

    def clean(self):
        if self.amount > self.game.quantity:
            raise ValidationError('The amout that you are trying to rent is greater than the amount in stock')

    def save(self, *args, **kwargs):
        self.clean()
        self.game.quantity -= self.amount
        if self.game.quantity < 0:
            raise ValidationError('Not enough copies in stock')
        self.game.save()
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.game.quantity += self.amount
        self.game.save()
        super().delete(*args, **kwargs)

