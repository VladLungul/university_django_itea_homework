from django.shortcuts import render
from .forms import StudentForm, TeacherForm
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.messages import get_messages

class StudentView(View):
    form_class = StudentForm
    template_name = 'university/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Student adding success')
            #return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})


class TeacherView(View):
    form_class = TeacherForm
    template_name = 'university/index.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages = get_messages(request)
            for m in messages:
                print(m)
            messages.add_message(request, messages.INFO, 'Teacher adding success')

        return render(request, self.template_name, {'form': form})


