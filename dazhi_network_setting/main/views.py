from django.views.generic import *
from .models import *
from django.contrib.auth.models import User


# Create your views here.

class Home(TemplateView):
    template_name = 'home'

class DeviceAdd(CreateView):
    model = Device
    fields = ["d_name" , "MAC"]

class DeviceDetail(DetailView):
    model = Device

class DeviceDelete(DeleteView):
    model = Device

class GroupList(ListView):
    model = Group

class GroupDelete(DeleteView):
    model = Group

class GroupCreate(CreateView):
    model = Group
    fields = ["g_name"]

class UserDetail(DetailView):
    model = User

class UserDelete(DeleteView):
    model = User

class UserAdd(CreateView):
    model = User

class UserList(ListView):
    model = User

class Upload():
    model = User