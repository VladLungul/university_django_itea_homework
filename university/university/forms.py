from django import forms

class Teacher(forms.Form):
    first_name = forms.CharField(label='Name', max_length=150)
    last_name = forms.CharField(label='Surname', max_length=30)
    subject = forms.CharField(label='Subject', max_length=30)
    email = forms.EmailField(label='Email', max_length=25)
    phone_number = forms.CharField(label='Phonenumber', max_length=30)


class Student(forms.Form):
    first_name = forms.CharField(label='Name', max_length=150)
    last_name = forms.CharField(label='Surname', max_length=30)
    avg_mark = forms.CharField(label='AVG_Mark', max_length=30)
    email = forms.EmailField(label='Email', max_length=25)
    phone_number = forms.CharField(label='Phonenumber', max_length=30)