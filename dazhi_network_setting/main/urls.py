from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view()),
    path('device/', DeviceHome.as_view(), name='d_home'),
    path('device/edit/', DeviceAdd.as_view(), name='d_edit'),
    path('device/list/', DeviceList.as_view(), name='d_list'),
    path('user/', UserHome.as_view(), name='u_home'),
    path('user/edit/', UserAdd.as_view(), name='u_edit'),
]