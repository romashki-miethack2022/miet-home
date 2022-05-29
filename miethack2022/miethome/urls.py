from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('schematic_search', schematic_search, name='schematic_search'),
    path('add_student', add_student, name='add_student'),
    path('get_floor', get_floor, name="get_floor"),
    path('get_rooms', get_rooms, name="get_rooms"),
]
