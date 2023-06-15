from django.views.generic import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class EditDevice_t(TemplateView):
    template_name = 'main/device_edit_t.html'

class EditUser_t(TemplateView):
    template_name = 'main/user_edit_t.html'

class DeviceAdd(LoginRequiredMixin, CreateView):
    template_name = 'main/device_edit.html'
    model = Device
    fields = ["d_name" , "MAC"]

class DeviceDetail(DetailView):
    model = Device

class DeviceList(ListView):
    template_name = 'main/device_list.html'
    model = Device

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
    template_name = 'main/user_edit.html'
    model = User
    
class UserList(LoginRequiredMixin, ListView):
    model = User

class Upload(LoginRequiredMixin, FormView):
    model = User