import logging
from django.shortcuts import render
from .forms import StudentForm, TeacherForm
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.contrib.messages import get_messages

logger = logging.getLogger(__name__)

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
            logger.info("Students info is right")
            messages.add_message(request, messages.INFO, 'Student adding success')
            #return HttpResponseRedirect('/success/')
        else:
            logger.warning("Students info is wrong!")

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
            logger.info("Teachers info is right")
            messages = get_messages(request)
            for m in messages:
                print(m)
            messages.add_message(request, messages.INFO, 'Teacher adding success')
        else:
            logger.warning("Teachers info is wrong!")


        return render(request, self.template_name, {'form': form})


