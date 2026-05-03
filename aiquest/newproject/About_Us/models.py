from django.db import models

# Create your models here.

class Teachers(models.Model):
    tid = models.ImageField()
    tname = models.CharField(max_length=50)
    temail = models.EmailField(max_length=30)

  