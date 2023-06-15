from django.views.generic import *
from .models import *
from django.contrib.auth.models import User


# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class EditDevice_t(TemplateView):
    template_name = 'main/device_edit_t.html'

class EditUser_t(TemplateView):
    template_name = 'main/user_edit_t.html'
class DeviceAdd(CreateView):
    template_name = 'main/device_edit.html'
    model = Device
    fields = ["d_name" , "MAC"]

class DeviceDetail(DetailView):
    model = Device

class DeviceList(ListView):
    template_name = 'main/device_list.html'
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
    template_name = 'main/user_edit.html'
    model = User
    
class UserList(ListView):
    model = User

class Upload():
    model = User