from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Restaurant(models.model):
    name = models.CharField(_MAX_LENGTH=30)
    description = models.TextField(default="")
    openning_time = models.TimeField()
    closing_time = models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)

    