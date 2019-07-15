from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Login(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    Email = models.EmailField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return str(self.id)