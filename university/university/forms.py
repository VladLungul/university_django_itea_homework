from django import forms
from .models import Student, Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'subject')


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'avg_mark')