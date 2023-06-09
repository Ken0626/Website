from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import *

# Create your views here.

#add_device delete_device device_detail device_list 
#add_user delete_user user_detail user_list
#

class DeviceAdd(CreateView):
    model = Device
    fields = ["d_name" , "MAC"]

class Device(DeleteView):
    model = Device

class DeviceDetail(DetailView):
    model = Device

class DeviceList(ListView):
    model = Device


