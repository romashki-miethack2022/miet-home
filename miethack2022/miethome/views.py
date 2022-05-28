from django.shortcuts import render

header = [
    {'title': 'Графический поиск', 'url_name': 'home'},
    {'title': 'Поиск по форме', 'url_name': 'schematic_search'}
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
