from datetime import datetime
from pyexpat import model
from django.db import models

# Create your models here.

class BaseField(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta():
        abstract = True

