from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT)

