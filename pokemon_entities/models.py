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
    level = models.IntegerField(default=1)
    health = models.IntegerField(default=100)
    strength = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    stamina = models.IntegerField(default=1)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.pokemon.name} по координатам ' \
               f'{self.longitude},{self.latitude}'
