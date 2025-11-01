from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Diary(models.Model):
    patient = models.OneToOneField(
        'users.Patient',
        on_delete=models.CASCADE,
        related_name='diary',
        unique=True
    )
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.patient} diary'


class Note(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    glycemic_level = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(50.0)]
    )
    insulin_injection_count = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        null=True,
        blank=True
    )
    diary = models.ForeignKey(
        Diary,
        on_delete=models.CASCADE,
        related_name='notes',
    )
    comment = models.TextField(blank=True, max_length=300)

    class Meta:
        ordering = ['-date']
