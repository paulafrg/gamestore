from django.db import models

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

    def __str__(self):
        return self.game
    
class Customers(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=150, blank=False, null=False)
    dob = models.DateField(default='%m/%d/%Y', blank=False, null=False)

    def __str__(self):
        return self.name

