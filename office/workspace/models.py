from django.db import models

class Office(models.Model):
    number = models.IntegerField(unique = False)
    address = models.CharField(max_length = 255)
    def __str__(self):
        return "№" + str(self.number)+ " (" + self.address + ")"
        
class Room(models.Model):
    number = models.IntegerField()
    number_of_sits = models.IntegerField()
    office = models.ForeignKey('Office', on_delete=models.CASCADE)
    def __str__(self):
        return "Office №" + str(self.office.number) + ". Room №" + str(self.number)

class Booked(models.Model):
    TIME = [
        (7, '7:00'), (8, '8:00'), (9, '9:00'), (10, '10:00'),
        (11, '11:00'), (12, '12:00'),(13, '13:00'), (14, '14:00'),
        (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'),
        (19, '19:00'), (20, '20:00'), (21, '21:00'), (22, "22:00"),
    ]
    date = models.DateField(default=None)
    time_from = models.IntegerField(choices = TIME)
    time_to = models.IntegerField(choices = TIME)
    worker_at = models.ForeignKey('worker.Worker', on_delete=models.CASCADE, default=None)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.worker_at.name + " " + self.worker_at.last_name + ". " + self.room.__str__() + ". Date: " + str(self.date) + ". Time: " + str(self.time_from) + " - " + str(self.time_to) 