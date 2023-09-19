from django.db import models
from django.utils import timezone

class contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=60)
    emial = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'