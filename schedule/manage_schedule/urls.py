from django.urls import path

from . import views


app_name = 'manage_schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]
