from django.urls import path

from chat import views

app_name = 'chat'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.create_view, name='create'),
    path('room/', views.RoomView.as_view(), name='room'),
    path('redirect/', views.redirect_view, name='redirect'),
    path('enter/', views.enter_view, name='enter'),
]
