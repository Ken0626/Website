import pyexcel as px

from django.http import HttpResponse
from typing import Type
from django.views.generic import *
from .models import Device
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin

from .forms import GetExcelForm

# 限定管理員才允許操作的混成類別
class SuperuserRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class DeviceHome(LoginRequiredMixin, TemplateView):
    template_name = 'main/device_home.html'

class GroupHome(LoginRequiredMixin, TemplateView):
    template_name = "main/group_home.html"

class UserHome(LoginRequiredMixin, TemplateView):
    template_name = 'main/user_home.html'

class DeviceAdd(LoginRequiredMixin, CreateView):
    model = Device
    template_name = 'main/device_create.html'
    fields = ["d_name" , "MAC"]

    success_url = '../list/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class DeviceDetail(LoginRequiredMixin, DetailView):
    model = Device
    template_name = 'main/device_detail.html'

class DeviceList(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'main/device_list.html'

class DeviceDelete(SuperuserRequiredMixin, DeleteView):
    model = Device

class GroupList(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'main/group_list.html'

class GroupDelete(SuperuserRequiredMixin, DeleteView):
    model = Group

class GroupCreate(SuperuserRequiredMixin, CreateView):
    model = Group
    fields = ["name"]
    template_name = 'main/group_create.html'



class UserDetail(LoginRequiredMixin, DetailView):
    model = User

class UserDelete(SuperuserRequiredMixin, DeleteView):
    model = User

class UserAdd(SuperuserRequiredMixin, CreateView):
    model = User
    template_name = 'main/user_create.html'
    fields=['groups', 'username', 'first_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["groups"] = Group.objects.all()
        return context
    

    def get_form(self):
        form = super().get_form()
        for field in form.fields:
            # if field == 'groups':
            #     continue
            form.fields[field].widget.attrs.update({'class': 'form-control'})
        return form
    
    def form_vaild(self, form):
        user = form.save(commit=False)
        user.set_password(form.instance.username)
        return super().form_valid(form)


    
class UserList(LoginRequiredMixin, ListView):
    template_name = 'main/user_list.html'
    model = User

class Upload(SuperuserRequiredMixin, FormView):
    template_name = 'form.html'
    form_class = GetExcelForm
    success_url = '../../'

    # def get_form(self):
    #     form = super().get_form()
    #     return form
    
    def form_valid(self, form):
        # print("!!!!")
        s = form.files['file']
        ext = s.name.split('.')[-1]
        content = s.read()
        sheets = px.get_records(file_type=ext, file_content=content)

        

        for sheet in sheets:
            exists_groups = list(Group.objects.all())
            # group = Group(g_name=sheet['所屬班級/單位'])
            match_group = list(filter(lambda g: g.name == str(sheet['所屬班級/單位']), exists_groups))
            if match_group:
                group = match_group[0]
            else:
                group = Group(name=sheet['所屬班級/單位'])
                group.save()

            try:
                user = User(first_name=sheet['學生/教師姓名'], 
                            username=sheet['學號/教師代碼'])
                user.set_password(str(sheet['學號/教師代碼']))
                user.save()
                user.groups.add(group)
            except:
                user = User.objects.get(username=sheet['學號/教師代碼'])
                user.groups.add(group)
                user.save()
        return super().form_valid(form)


