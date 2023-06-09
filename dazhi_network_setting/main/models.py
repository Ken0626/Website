from django.db import models

# Create your models here.

class Group(models.Model):
    g_name = models.CharField("班級/群組")

class User(models.Model):
    name = models.CharField("使用者姓名", max_length=10)
    groups = models.ForeignKey(Group, models.CASCADE)
    
class Device(models.Model):
    d_name = models.CharField("裝置型號", max_length=25)
    owner = models.ForeignKey(User)
    MAC = models.CharField("MAC" , max_length=20)




