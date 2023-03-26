from django.urls import path
from technologies import views

app_name = 'technologies'

urlpatterns = [
    path('', views.index, name='index')
]