from django.contrib import admin
from .models import Student, Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name')
    ordering = ('first_name',)
    list_display_links = list_display

admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
