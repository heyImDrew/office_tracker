from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    booked_history = models.ManyToManyField('workspace.Booked', blank = True)
    def __str__(self):
        return self.name + " " + self.last_name