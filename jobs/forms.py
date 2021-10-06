from typing import Text
from django import forms

class TodoListForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget = forms.TextInput(
            attrs={'class': 'form-control','placeholder':'enter todo e.g Grocery shoping','aria-label':'Todo','aria-describeby':'add-btn' }))