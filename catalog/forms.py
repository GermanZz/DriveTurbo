from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from catalog.models import Advertisement
from django.utils import timezone
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AdvertForm(forms.ModelForm):
    """ Creation of advertisements is done by this form """
    class Meta:
        model = Advertisement
        fields = ['brand', 'body_type', 'gear_box', 'drive', 'color', 'cover_img', 'year', 'mileage', 'engine_capacity',
                  'description', 'price']

        widgets = {'brand': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Введите год'}),
                   'body_type': forms.Select(attrs={'class': 'form-control'}),
                   'gear_box': forms.Select(attrs={'class': 'form-control'}),
                   'drive': forms.Select(attrs={'class': 'form-control'}),
                   'color': forms.Select(attrs={'class': 'form-control'}),
                   'cover_img': forms.FileInput(attrs={'class': 'form-control-file', 'type': 'file'}),
                   'year': forms.NumberInput(attrs={'class': 'form-control'}),
                   'mileage': forms.NumberInput(attrs={'class': 'form-control'}),
                   'engine_capacity': forms.Select(attrs={'class': 'form-control'}),
                   'description': CKEditorUploadingWidget(
                       attrs={'class': 'form-control', 'rows': '10'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control'}),
                   }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError('Цена не может быть меньше или равна нулю!')
        return price

    def clean_mileage(self):
        mileage = self.cleaned_data['mileage']
        if mileage < 0:
            raise forms.ValidationError('Пробег не может быть меньше или равна нулю!')
        return mileage

    def clean_year(self):
        year = self.cleaned_data['year']
        if not (1900 < year <= timezone.now().year):
            raise forms.ValidationError('Введите корректный год!')
        return year


class UserRegisterForm(UserCreationForm):
    """ User Registration Form """
    username = forms.CharField(label='Введите имя пользователя:',
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label='Имя:',
                                 widget=forms.TextInput(attrs={"class": "form-control", "autofocus": "True"}))
    last_name = forms.CharField(label='Фамилия:',
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label='Введите Email:',
                             widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Введите пароль:',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Подтвердите пароль:',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]


class UserLoginForm(AuthenticationForm):
    """ User Login Form """
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    field_order = ['username', 'password']
