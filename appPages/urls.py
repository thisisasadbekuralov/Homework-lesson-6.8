from django.urls import path

from .views import index, index_ru, index_eng, index_uz

urlpatterns = [
    path('weekdays/', index, name='index_url'),
    path('weekdays_ru/', index_ru, name='index_url'),
    path('weekdays_eng/', index_eng, name='index_url'),
    path('weekdays_uz/', index_uz, name='index_url'),

]


