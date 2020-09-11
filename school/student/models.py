from django.db import models
# Create your models here.
class registration(models.Model):
    firstname = models.CharField(max_length = 30);
    lastname = models.CharField(max_length = 30);
    username = models.CharField(max_length = 30);
    password = models.CharField(max_length= 30);
    confirm_password = models.CharField(max_length = 30);
    email = models.CharField(max_length=30);
    def __str__(self):
        return self.username
