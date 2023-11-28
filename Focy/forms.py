from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["Name", "Phone_number", "Email", "Message"]
    labels = {'Name': "Name", "Phone_number": "Phone Number", "Email": "Email", "Message": "Message"}