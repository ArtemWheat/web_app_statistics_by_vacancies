from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('demand/', views.demand, name='demand'),
    path('geography', views.geography, name='geography'),
    path('key_skills', views.key_skills, name='key_skills'),
    path('vacancies', views.vacancies, name='vacancies')
]
