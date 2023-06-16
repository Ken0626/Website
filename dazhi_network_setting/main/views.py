import pyexcel as px

from django.http import HttpResponse
from typing import Type
from django.views.generic import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import GetExcelForm

# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class DeviceHome(TemplateView):
    template_name = 'main/device_home.html'

class UserHome(TemplateView):
    template_name = 'main/user_home.html'

class DeviceAdd(LoginRequiredMixin, CreateView):
    model = Device
    template_name = 'main/device_create.html'
    fields = ["d_name" , "MAC"]

    success_url = '../list/'

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
    template_name = 'main/user_create.html'
    fields=['groups', 'username', 'first_name']

    def get_form(self):
        form = super().get_form()
        for field in form.fields:
            # if field == 'groups':
            #     continue
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form
    
    def form_vaild(self, form):
        number = form.files['username']
        form.instence.password
        return super.form_vaild(form)

    
class UserList(LoginRequiredMixin, ListView):
    model = User

class Upload(LoginRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = GetExcelForm

    def get_form(self):
        form = super().get_form()
        return form
    
    def form_valid(self, form):
        s = form.instance.file

