from django.views.generic import *
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = 'main/home.html'

class DeviceAdd(CreateView):
    model = Device
    fields = ["d_name" , "MAC"]

class Device(DeleteView):
    model = Device

class DeviceDetail(DetailView):
    model = Device

class DeviceList(ListView):
    model = Device

