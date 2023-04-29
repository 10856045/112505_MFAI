from django.shortcuts import render
from django.http import HttpResponse


def my_path(request):
    name = request.POST.get('name', 'Unknown')
    return render(
        request, 
        'my_path.html', 
        {
            'name': name, 
            'data': [1, 2, 3, 4, 5],
            'ok': True,
        },
    )


def add(request, n1, n2):
    return HttpResponse(n1 + n2)


def minus(request, n1, n2):
    return HttpResponse(n1 - n2)


def multiplied_by(request, n1, n2):
    return HttpResponse(n1 * n2)


def divided_by(request, n1, n2):
    return HttpResponse(n1 / n2)