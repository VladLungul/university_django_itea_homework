from .views import StudentView, TeacherView
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
 path('student/', StudentView.as_view(), name="add_student"),
 path('teacher/', login_required(TeacherView.as_view(),login_url='/login'), name="add_teacher")

]