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
    path('device/number<int:pk>/update/', DeviceUpdate.as_view(), name='d_update'),
    path('device/number<int:pk>/delete/', DeviceDelete.as_view(), name='d_delete'),

    path('user/', UserHome.as_view(), name='u_home'),
    path('user/create/', UserAdd.as_view(), name='u_create'),
    path('user/list/', UserList.as_view(), name='u_list'),
    path('user/number<int:pk>/device/', UserDevice.as_view(), name='u_device'),
    path('user/number<int:pk>/update/', UserUpdate.as_view(), name='u_update'),
    path('user/number<int:pk>/delete/', UserDelete.as_view(), name='u_delete'),

    path('group/', GroupHome.as_view(), name='g_home'),
    path('group/create/', GroupCreate.as_view(), name='g_create'),
    path('group/list/', GroupList.as_view(), name='g_list'),
    path('group/number<int:pk>/user/', GroupUser.as_view(), name='g_user'),
    path('group/number<int:pk>/update/',GroupUpdate.as_view(),name='g_update'),
    path('group/number<int:pk>/delete/',GroupDelete.as_view(),name='g_delete'),
    
]   