from django import forms
from .models import *

class GetExcelForm(forms.Form):
    file = forms.FileField(label='上傳學生與教師註冊活頁簿')