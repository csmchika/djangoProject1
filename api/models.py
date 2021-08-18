from django.db import models


class Activity(models.Model):

    class Type(models.TextChoices):
        RUN = 'Бег',
        WALK = 'Ходьба',
        BICYCLE = 'Велосипед'

    type = models.CharField(choices=Type.choices, max_length=25, default='null')
    name = models.CharField(max_length=15, default='Активность')
    started = models.TimeField(blank=True,)
    finished = models.TimeField(auto_now_add=True)
    distance = models.FloatField(blank=True,)
    owner = models.ForeignKey('auth.User', related_name='activity', on_delete=models.CASCADE)

    class Meta:
        # ordering = ['created']
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

    def __str__(self):
        return 'Активность %s типа %s' % (self.owner, self.type)
