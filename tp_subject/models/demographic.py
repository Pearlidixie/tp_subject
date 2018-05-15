from django.db import models
from tp_subject.choices import MARITAL_STATUS, LIVES_WITH


class Demographic(models.Model):

    marital_status = models.CharField(
        max_length=50,
        choices=MARITAL_STATUS)

    number_husbands = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="If subject is a woman, how many wives does the husband have (traditional wives and subject included)",)

    number_wives = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="If subject is a man, how many wives does he have (traditional marriage included)?",)

    lives_with = models.CharField(
        max_length=10,
        verbose_name="Who do you currently live with?",
        choices=LIVES_WITH)