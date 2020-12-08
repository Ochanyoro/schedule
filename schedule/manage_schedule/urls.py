from django.urls import path

from . import views


app_name = 'manage_schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(),name='inquiry'),
    path('schedule-list/', views.ScheduleListView.as_view(), name="schedule_list"),
    path('schedule-create/',views.ScheduleCreateView.as_view(),name='schedule_create'),
]
