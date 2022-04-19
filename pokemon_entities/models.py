from django.db import models


class Pokemon(models.Model):
    name = models.CharField('Название', max_length=100)
    en_name = models.CharField('Название на английском', max_length=100)
    jp_name = models.CharField('Название на японском', max_length=100)
    description = models.TextField('Описание')
    previous_evolution = models.ForeignKey(
        'self',
        verbose_name='Эволюционировал из',
        on_delete=models.SET_NULL,
        null=True,
        related_name='next_evolution',
    )
    image = models.ImageField('Изображение', null=True)

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):
    latitude = models.FloatField('Долгота')
    longitude = models.FloatField('Широта')
    appeared_at = models.DateTimeField('Появился в')
    disappeared_at = models.DateTimeField('Исчез в')
    level = models.IntegerField('Уровень', default=1)
    health = models.IntegerField('Жизни', default=100)
    strength = models.IntegerField('Сила', default=1)
    defence = models.IntegerField('Защита', default=1)
    stamina = models.IntegerField('Выносливость', default=1)
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.pokemon.name} по координатам ' \
               f'{self.longitude},{self.latitude}'
