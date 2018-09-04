from django.shortcuts import render
from .forms import StudentForm, TeacherForm
from django.http import HttpResponseRedirect
from django.views import View


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
            return HttpResponseRedirect('/success/')

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
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

