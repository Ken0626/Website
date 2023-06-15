from django.views.generic import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class DeviceHome(TemplateView):
    template_name = 'main/device_home.html'

class UserHome(TemplateView):
    template_name = 'main/user_home.html'

class DeviceAdd(LoginRequiredMixin, CreateView):
    model = Device
    template_name = 'main/device_edit.html'
    fields = ["d_name" , "MAC"]

class DeviceDetail(DetailView):
    model = Device
    template_name = 'main/device_detail.html'

class DeviceList(ListView):
    model = Device
    template_name = 'main/device_list.html'

class DeviceDelete(LoginRequiredMixin, DeleteView):
    model = Device

class GroupList(ListView):
    model = Group

class GroupDelete(LoginRequiredMixin, DeleteView):
    model = Group

class GroupCreate(LoginRequiredMixin, CreateView):
    model = Group
    fields = ["g_name"]

class UserDetail(LoginRequiredMixin, DetailView):
    model = User

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User

class UserAdd(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'main/user_edit.html'
    
class UserList(LoginRequiredMixin, ListView):
    model = User

class Upload(LoginRequiredMixin, FormView):
    model = User