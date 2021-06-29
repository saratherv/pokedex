from django.db import models
# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    typeOne = models.CharField(max_length=100)
    typeTwo = models.CharField(max_length=100)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    specialAttack = models.IntegerField()
    specialDefense = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    isLegendary = models.BooleanField()

    def __str__(self) -> str:
        return super().__str__()



