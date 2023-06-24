from django.urls import path, include
from .views import *

urlpatterns = [
    path('form/', Upload.as_view(), name='form'),
    path('', Home.as_view()),

    path('device/', DeviceHome.as_view(), name='d_home'),
    path('device/create/', DeviceAdd.as_view(), name='d_create'),
    path('device/list/', DeviceList.as_view(), name='d_list'),
    path('device/listall/', DeviceListAll.as_view(), name='d_list_all'),
    path('device/add/', DeviceAdd.as_view(), name='d_add'),
    path('device/number<int:pk>/', DeviceDetail.as_view(), name='d_detail'),
    path('device/number<int:pk>/delete/', DeviceDelete.as_view(), name='d_delete'),

    path('user/', UserHome.as_view(), name='u_home'),
    path('user/create/', UserAdd.as_view(), name='u_create'),
    path('user/list/', UserList.as_view(), name='u_list'),
    path('user/number<int:pk>/device/', User_Device.as_view(), name='u_device'),

    path('group/', GroupHome.as_view(), name='g_home'),
    path('group/create/', GroupCreate.as_view(), name='g_create'),
    path('group/list/', GroupList.as_view(), name='g_list'),
]   