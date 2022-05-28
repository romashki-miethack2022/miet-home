from django.shortcuts import render, redirect

from miethome.forms import AddStudentForm, SearchForm
from miethome.models import Student, Room

header = [
    {'title': 'Графический поиск', 'url_name': 'home'},
    {'title': 'Поиск по форме', 'url_name': 'schematic_search'},
    {'title': 'Добавление студента', 'url_name': 'add_student'}
]


def index(request):
    context = {
        'title': "Поиск по форме",
        'header': header,
    }

    return render(request, 'miethome/index.html', context=context)


def schematic_search(request):
    context = {
        'title': "Графический поиск",
        'header': header,
    }

    return render(request, 'miethome/schematic_search.html', context=context)


def add_student(request):
    form = AddStudentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            room = Room.objects.create(room_number=form.cleaned_data['room_room'],
                                       corpus_number=form.cleaned_data['room_corpus'])
            Student.objects.create(id=form.cleaned_data['stud_id'],
                                   full_name=form.cleaned_data['full_name'],
                                   birth_date=form.cleaned_data['birth_date'],
                                   home_order_number=form.cleaned_data['home_order_number'],
                                   enrollment_order_number=form.cleaned_data['enrollment_order_number'],
                                   date_enrollment=form.cleaned_data['date_enrollment'],
                                   birth_place=form.cleaned_data['birth_place'],
                                   room=room,
                                   )
        else:
            form = AddStudentForm()
            form.add_error(None, 'Ошибка добавления нового элемента!')

    context = {
        'title': "Добавление студента",
        'header': header,
        'form': form
    }
    return render(request, 'miethome/add_student.html', context=context)


def schematic_search(request):
    matches = set()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Поиск совпадений полей формы с бд
            data = form.cleaned_data
            print(data)
            keys = data.keys()
            for key in keys:
                if data[key]:
                    my_filter = {key: data[key]}
                    student = Student.objects.filter(**my_filter)
                    if student:
                        print(f"Найдено совпадение: {student}")
                        matches.add(student)
                    else:
                        print("Нет ничего")

        print(matches)

    else:
        form = SearchForm()

    context = {
        'title': "Графический поиск",
        'header': header,
        'form': form,
    }

    return render(request, 'miethome/schematic_search.html', context=context)
