from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def task(request):
    units = Units.objects.all()
    return render(request, 'task.html', {"units": units})


def test(request):
    units = Units.objects.all()
    return render(request, 'test.html', {"units": units})


def show_task(request, unit_name):
    tasks = Tasks.objects.all()
    units = Units.objects.all()
    return render(request, 'show_task.html', {"tasks": tasks, "unit_name": unit_name, "units": units})


def theory(request):
    units = Units.objects.all()
    return render(request, 'theory.html', {"units": units})


def show_test(request, unit_name):
    units = Units.objects.all()
    test = Tests.objects.all()
    if request.method == 'POST':
        count = 0
        cor = {}
        nocor = {}
        l = request.POST
        for i in l:
            print(l[i])
            for j in range(len(test)):
                if i == test[j].radio:
                    if l[i] == test[j].correct:
                        cor[test[j].radio] = f'{test[j].question} {l[i]}'
                        count += 1
                    else:
                        nocor[
                            test[j].radio] = f'{test[j].question} Ваш ответ: {l[i]} Правильный ответ: {test[j].correct}'

        return render(request, 'posts_result.html',
                      {"count": count, "unit_name": unit_name, "cor": cor, "nocor": nocor})
    else:
        return render(request, 'show_test.html', {"unit_name": unit_name, "units": units, "test": test})
