from django.db import models

# Create your models here.
class Cric(models.Model):
    team1 = models.TextField(max_length = 50)
    
