from django.forms import ModelForm
from .models import Todo


class TodoForm(ModelForm):
    """This is for creating our personilized form specific for out model"""
    class Meta:
        model = Todo
        fields = ['title',  'memo', 'important']