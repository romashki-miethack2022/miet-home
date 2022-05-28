from django.db import models

# Create your models here.


class Room(models.Model):
    """Represents direction disciplines (subjects) in database"""
    room_number = models.IntegerField()
    corpus_number = models.IntegerField()

    def __str__(self):
        return f'{self.room_number}->{self.corpus_number}'


class Student(models.Model):
    """Represents Man in database"""
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=10)
    img = models.ImageField(upload_to='static/img/students_photo/')
    home_order_number = models.CharField(max_length=20)
    enrollment_order_number = models.CharField(max_length=10)
    date_enrollment = models.CharField(max_length=10)
    birth_place = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.id)



