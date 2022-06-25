from django.db import models

# Create your models here.

# En la terminal de Postgres, para conectarte a la bd es: \c tasksdb

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
