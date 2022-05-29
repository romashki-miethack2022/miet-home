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
    id = models.IntegerField(primary_key=True, verbose_name='Номер карточки')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    birth_date = models.CharField(max_length=10, verbose_name='Дата рождения')
    img = models.ImageField(upload_to='static/img/students_photo/', verbose_name='Фото')
    home_order_number = models.CharField(max_length=20, verbose_name='Номер приказа о предоставлении общежития')
    enrollment_order_number = models.CharField(max_length=10, verbose_name='Номер приказа о зачислении')
    date_enrollment = models.CharField(max_length=10, verbose_name='Дата зачисления')
    birth_place = models.CharField(max_length=100, verbose_name='Место рождения')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, verbose_name='Адрес проживания')

    def __str__(self):
        return str(self.id)



