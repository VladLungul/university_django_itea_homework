from django.db import models
from django.core.validators import MaxValueValidator
import logging

logger = logging.getLogger(__name__)

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    phone_number = models.CharField(max_length=25,blank=True)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name},{self.subject}, {self.email}, {self.phone_number})'
    def __repr__(self):
        return self.__str__()
  #  def clean(self):
   #       if not phone_validation(self.phone_number):
    #        raise ValidationError('Phone is incorrect')
    def saving(self):
        self.save()




class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    email = models.EmailField(max_length=25)
    phone_number = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name},{self.avg_mark}, {self.email}, {self.phone_number})'
    def __repr__(self):
        return self.__str__()
  #  def clean(self):
   #     if not phone_validation(self.phone_number):
    #        raise ValidationError('Phone is incorrect')
    def saving(self):
        self.save()