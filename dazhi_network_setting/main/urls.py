from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view()),
    path('device_edit_t/',EditDevice_t.as_view()),
    path('device_edit/',DeviceAdd.as_view()),
    path('device_list/',DeviceList.as_view()),
    path('user_edit_t/',EditUser_t.as_view()),
    path('user_edit/',UserAdd.as_view()),
]