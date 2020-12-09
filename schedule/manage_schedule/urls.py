from django.urls import path

from . import views


app_name = 'manage_schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(),name='inquiry'),
    path('month/',views.MonthCalendar.as_view(),name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
]


"""
path('calender/',views.Calender.as_view(),name='mycalender'),
path('calender/<int:year>/<int:month>/<int:day>/',views.Calender.as_view(),name='mycalender')
"""
