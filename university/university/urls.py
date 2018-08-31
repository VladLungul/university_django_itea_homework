from django.urls import path
from . import views
urlpatterns = [
 path('university/', views.my_index_view, name='index')
]