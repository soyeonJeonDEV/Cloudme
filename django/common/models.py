from django.db import models


from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    is_admin = models.BooleanField(default=False)

# Create your models here.
