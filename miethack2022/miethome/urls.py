from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('schematic_search/', schematic_search, name='schematic_search')
]
