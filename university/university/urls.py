from .views import StudentView, TeacherView, ClasView
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
 path('student/', StudentView.as_view(), name="student"),
 path('teacher/', login_required(TeacherView.as_view(),login_url='/login/'), name="teacher"),
 path('clas/', ClasView.as_view(), name="clas"),

]