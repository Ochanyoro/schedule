from django.urls import path

from . import views


app_name = 'manage_schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('inquiry/', views.InquiryView.as_view(),name='inquiry'),
    path('month/',views.MonthCalendar.as_view(),name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('week/', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),
    path('week_with_schedule/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path(
        'week_with_schedule/<int:year>/<int:month>/<int:day>/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    ),
    path(
        'month_with_schedule/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthWithScheduleCalendar.as_view(), name='month_with_schedule'
    ),
    path('mycalendar/', views.MyCalendar.as_view(), name='mycalendar'),
    path(
        'mycalendar/<int:year>/<int:month>/<int:day>/', views.MyCalendar.as_view(), name='mycalendar'
    ),

    path('management/',views.ManagementView.as_view(),name='management'),
]


"""
path('calender/',views.Calender.as_view(),name='mycalender'),
path('calender/<int:year>/<int:month>/<int:day>/',views.Calender.as_view(),name='mycalender')
"""
