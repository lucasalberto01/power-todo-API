from django.db import models

# Create your models here.


class List(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name
