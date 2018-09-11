from django.db import models
from django.core.validators import MaxValueValidator, ValidationError
import logging
import re

logger = logging.getLogger(__name__)

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=25)
    phone_number = models.CharField(max_length=25, blank=True)

    class Meta:
        abstract = True
    def my_validator(self, val, value_valid):
        is_match = value_valid.search(val)
        return is_match

    first_name_valid = re.compile(r'^[A-z]+\ ?[A-z]?$')
    phone_valid = re.compile(r'^\+380\d{9}$')
    last_name_valid = re.compile(r'^[A-z]+\-?[A-z]?$')


    def clean(self):
        if not self.my_validator(self.phone_number, self.phone_valid):
            logger.warning('bad user, wrong data number')
            raise ValidationError('not correct number')
        if not self.my_validator(self.first_name, self.first_name_valid):
            logger.warning('bad user, wrong data first name')
            raise ValidationError('not correct first name')
        if not self.my_validator(self.last_name, self.last_name_valid):
            logger.warning('bad user, wrong data last name')
            raise ValidationError('not correct last_name')


class Teacher(Person):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name},{self.subject}, {self.email}, {self.phone_number})'
    def __repr__(self):
        return self.__str__()

class Clas(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f'S({self.name})'
    def __repr__(self):
        return self.__str__()



class Student(Person):
    avg_mark = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    clas = models.ForeignKey(Clas, on_delete=models.CASCADE)

    def __str__(self):
        return f'S({self.first_name}, {self.last_name},{self.avg_mark}, {self.email}, {self.phone_number}, {self.clas})'
    def __repr__(self):
        return self.__str__()
