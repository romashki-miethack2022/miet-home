from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('schematic_search', schematic_search, name='schematic_search'),
    path('add_student', add_student, name='add_student'),
]
