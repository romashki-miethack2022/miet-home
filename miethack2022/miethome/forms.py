from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SearchForm(forms.Form):

    id = forms.IntegerField(required=False, widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер студентческого', 'class': 'input-data-field', 'name': 'student_id'})))
    full_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs=({'placeholder': 'ФИО', 'class': 'input-data-field', 'name': 'full_name'})))
    birth_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs=({'placeholder': 'Дата рождения', 'class': 'input-data-field', 'name': 'birth_date'})))
    home_order_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs=({'placeholder': 'Номер приказа заселения', 'class': 'input-data-field', 'name': 'home_order_number'})))
    enrollment_order_number = forms.CharField(required=False, widget=forms.TextInput(
        attrs=({'placeholder': 'Номер приказа зачисления', 'class': 'input-data-field', 'name': 'enrollment_order_number'})))
    date_enrollment = forms.DateField(required=False, widget=forms.DateInput(
        attrs=({'placeholder': 'Дата зачисления', 'class': 'input-data-field', 'name': 'date_enrollment'})))
    birth_place = forms.CharField(required=False, widget=forms.TextInput(
        attrs=({'placeholder': 'Место рождения', 'class': 'input-data-field', 'name': 'birth_place'})))
    room_room = forms.IntegerField(required=False, widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер комнаты', 'class': 'input-data-field', 'name': 'room_room'})))
    room_corpus = forms.IntegerField(required=False, widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер корпуса', 'class': 'input-data-field', 'name': 'room_corpus'})))


class AddStudentForm(forms.Form):
    stud_id = forms.IntegerField(widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер студенческого', 'class': 'input-data-field', 'name': 'student_id'})))
    full_name = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'ФИО', 'class': 'input-data-field', 'name': 'full_name'})))
    birth_date = forms.DateField(widget=forms.DateInput(
        attrs=({'placeholder': 'Дата рождения', 'class': 'input-data-field', 'name': 'birth_date'})))
    home_order_number = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Номер приказа заселения', 'class': 'input-data-field', 'name': 'home_order_number'})))
    enrollment_order_number = forms.CharField(widget=forms.TextInput(
        attrs=(
        {'placeholder': 'Номер приказа зачисления', 'class': 'input-data-field', 'name': 'enrollment_order_number'})))
    date_enrollment = forms.DateField(widget=forms.DateInput(
        attrs=({'placeholder': 'Дата зачисления', 'class': 'input-data-field', 'name': 'date_enrollment'})))
    birth_place = forms.CharField(widget=forms.TextInput(
        attrs=({'placeholder': 'Место рождения', 'class': 'input-data-field', 'name': 'birth_place'})))
    room_room = forms.IntegerField(widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер комнаты', 'class': 'input-data-field', 'name': 'room_room'})))
    room_corpus = forms.IntegerField(widget=forms.NumberInput(
        attrs=({'placeholder': 'Номер корпуса', 'class': 'input-data-field', 'name': 'room_corpus'})))