from cProfile import label
from dataclasses import field
from django import forms



class UploadFileForm(forms.Form):
    file = forms.FileField(required=False)