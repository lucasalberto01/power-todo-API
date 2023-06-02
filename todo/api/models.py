from django.db import models

# Create your models here.


class Task(models.Model):
    by_list = models.ForeignKey('list.List', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title
