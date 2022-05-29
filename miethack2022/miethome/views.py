from django.shortcuts import render, redirect

from miethome.forms import AddStudentForm, SearchForm, EditStudentForm
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
    form, students, msg = get_form_matches(request)

    context = {
        'title': "Схематичный поиск",
        'header': header,
        'form': form,
        'students': students,
        'matches_res': msg
    }

    return render(request, 'miethome/schematic_search.html', context=context)


def get_form_matches(request):
    students = []
    matches_res = ""

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Поиск совпадений полей формы с бд
            data = form.cleaned_data
            keys = data.keys()
            my_filters = {}
            # Добавляем все выставленные в форме фильтры
            for key in keys:
                if data[key]:
                    my_filters[key] = data[key]

            # Получаем из бд объекты, соответствующие фильтрам.
            # Если словарь с фильтрами пустой, то данные не выводятся (так как форма не была заполнена)
            if my_filters:
                students = Student.objects.filter(**my_filters)

            # Формируем сообщение пользователю о результате поиска
            if students:
                matches_res = "Найденные студенты:"
            else:
                matches_res = "Студенты с заданными фильтрами не найдены."

    else:
        form = SearchForm()

    return form, students, matches_res


def edit_student(request):
    form = EditStudentForm(request.POST, instance=Student)
    student = Student.objects.get(id=form.cleaned_data['id'])
    if form.is_valid():
        room = Room.objects.get(room_number=form.cleaned_data['room_room'],
                                corpus_number=form.cleaned_data['room_corpus'])
        student.save(id=form.cleaned_data['stud_id'],
                     full_name=form.cleaned_data['full_name'],
                     birth_date=form.cleaned_data['birth_date'],
                     home_order_number=form.cleaned_data['home_order_number'],
                     enrollment_order_number=form.cleaned_data['enrollment_order_number'],
                     date_enrollment=form.cleaned_data['date_enrollment'],
                     birth_place=form.cleaned_data['birth_place'],
                     room=room,
                     )
        context = {
            'title': "Схематичный поиск",
            'header': header,
        }
        return render(request, 'miethome/schematic_search.html', context=context)


def delete_student(request, id):
        st = Student.objects.get(id=id)
        st.delete()
        context = {
            'title': "Схематичный поиск",
            'header': header,
        }
        return render(request, 'miethome/schematic_search.html', context=context)
