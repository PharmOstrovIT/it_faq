from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


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
    """ Форма для добавления оборудования """

    class Meta:
        model = Equipment
        fields = ['apteka_id', 'equipment_type', 'equipment_model', 'serial_number', 'invoice_number',
                  'invoice_date', 'purchase_org', 'comments']

        widgets = {
            'apteka_id': forms.TextInput(attrs={'class': 'form-control', 'id': 'apteka_id',
                                                'name': 'apteka_id', 'placeholder': '1'}),
            'equipment_type': forms.TextInput(attrs={'class': 'form-control', 'id': 'equipment_type',
                                                     'name': 'equipment_type', 'placeholder': 'Принтер'}),
            'equipment_model': forms.TextInput(attrs={'class': 'form-control', 'id': 'equipment_model',
                                                      'name': 'equipment_model', 'placeholder': 'Xerox 3025'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'serial_number',
                                                    'name': 'serial_number', 'placeholder': 'Номер отсутствует'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'invoice_number',
                                                     'name': 'invoice_number', 'placeholder': '1234567890'}),
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'id': 'invoice_date',
                                                   'name': 'invoice_date', 'placeholder': '2022-01-01'}),
            'purchase_org': forms.TextInput(attrs={'class': 'form-control', 'id': 'purchase_org',
                                                   'name': 'purchase_org', 'placeholder': 'Не указан'}),
            'comments': forms.TextInput(attrs={'class': 'form-control', 'id': 'comments',
                                               'name': 'comments', 'placeholder': 'No Comments'}),
        }


class LanForm(ModelForm):
    """ Форма для локальной сети """

    class Meta:
        model = Security
        fields = ['apteka_id', 'service_name', 'service_ip', 'service_login', 'service_pass', 'service_info']

        widgets = {

            'apteka_id': forms.TextInput(attrs={'class': 'form-control select', 'id': 'apteka_id',
                                                'name': 'apteka_id', 'placeholder': '1'}),
            'service_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'service_name',
                                                   'name': 'service_name', 'placeholder': 'Принтер'}),
            'service_ip': forms.TextInput(attrs={'class': 'form-control', 'id': 'service_ip',
                                                 'name': 'service_ip', 'placeholder': '192.168.1.1'}),
            'service_login': forms.TextInput(attrs={'class': 'form-control', 'id': 'service_login',
                                                    'name': 'service_login', 'placeholder': 'Login'}),
            'service_pass': forms.TextInput(attrs={'class': 'form-control', 'id': 'service_pass',
                                                   'name': 'service_pass', 'placeholder': 'Password'}),
            'service_info': forms.TextInput(attrs={'class': 'form-control', 'id': 'service_info',
                                                   'name': 'service_info', 'placeholder': 'Нет информации'}),
        }


class LocationChoiceField(forms.Form):
    """ Получаем все названия аптек из базы данных и записываем их в переменную locations
    для дальнейшего использования в выпадающем списке.
    Если надо получить список уникальных значений добавляем distinct() в конец запроса.
    """

    locations = forms.ModelChoiceField(
        queryset=Apteka.objects.values_list("name", flat=True).order_by('id'),
        empty_label=None,
        required=True,
        label='Выберите аптеку')
