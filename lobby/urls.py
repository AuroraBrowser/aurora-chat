from django.urls import path

from lobby import views

app_name = 'lobby'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]
