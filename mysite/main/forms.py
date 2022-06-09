from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Equipment


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = ['apteka_id', 'equipment_type', 'equipment_model', 'serial_number', 'purchase_date', 'invoice_number',
                  'invoice_date', 'purchase_org', 'comments']

        widgets = {
            'apteka_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'apteka_id',
                                                'name': 'apteka_id', 'value': '1'}),
            'equipment_type': forms.TextInput(attrs={'class': 'form-control', 'id': 'equipment_type',
                                                     'name': 'equipment_type', 'value': 'Принтер'}),
            'equipment_model': forms.TextInput(attrs={'class': 'form-control', 'id': 'equipment_model',
                                                      'name': 'equipment_model', 'value': 'Xerox 3025'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'serial_number',
                                                    'name': 'serial_number', 'value': 'Номер отсутствует'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'invoice_number',
                                                     'name': 'invoice_number', 'value': '1234567890'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'id': 'invoice_date',
                                                   'name': 'invoice_date', 'value': '2022-01-01'}),
            'purchase_org': forms.TextInput(attrs={'class': 'form-control', 'id': 'purchase_org',
                                                   'name': 'purchase_org', 'value': 'ООО "Вася пупкин и компания"'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'id': 'comments',
                                               'name': 'comments', 'value': 'No Comments'}),
        }
