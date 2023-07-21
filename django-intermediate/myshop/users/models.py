from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.EmailField(max_length=70)
    full_name = models.CharField(max_length=70)
    birhtdate = models.DateField()
