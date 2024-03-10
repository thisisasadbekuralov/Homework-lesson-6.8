from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    language = '<a href="http://127.0.0.1:8000/weekdays_uz/">Uz</a>' '<br>'
    language += '<a href="http://127.0.0.1:8000/weekdays_ru/">Ru</a>' '<br>'
    language += '<a href="http://127.0.0.1:8000/weekdays_eng/">Eng</a>'
    return HttpResponse(language)

def index_ru(request):
    den = '<h1>Понедельник</h1>'
    den += '<h1>Вторник</h1>'
    den += '<h1>Среда</h1>'
    den += '<h1>Четверг</h1>'
    den += '<h1>Пятница</h1>'
    den += '<h1>Суббота</h1>'
    den += '<h1>Воскресенье</h1>'
    den += '<a href="http://127.0.0.1:8000/weekdays/">Back</a>'
    return HttpResponse(den)

def index_eng(request):
    day = '<h1>Monday</h1>'
    day += '<h1>Tuesday</h1>'
    day += '<h1>Wednesday</h1>'
    day += '<h1>Thursday</h1>'
    day += '<h1>Friday</h1>'
    day += '<h1>Satuday</h1>'
    day += '<h1>Sunday</h1>'
    day += '<a href="http://127.0.0.1:8000/weekdays/">Back</a>'
    return HttpResponse(day)

def index_uz(request):
    kun = '<h1>Dushanba</h1>'
    kun += '<h1>Seshanba</h1>'
    kun += '<h1>Chorshanba</h1>'
    kun += '<h1>Payshanba</h1>'
    kun += '<h1>Juma</h1>'
    kun += '<h1>Shanba</h1>'
    kun += '<h1>Yakshanba</h1>'
    kun += '<a href="http://127.0.0.1:8000/weekdays/">Back</a>'
    return HttpResponse(kun)