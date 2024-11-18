from django import forms
from django.contrib.auth.models import User
from .models import ProfileUser

class UserForm(forms.ModelForm):
    password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return cleaned_data

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['first_name', 'middle_name', 'last_name', 'phone', 'address', 'gender', 'birthdate', 'photo']

class EditProfileUserForm(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = ['first_name', 'middle_name', 'last_name', 'phone', 'address', 'gender', 'birthdate', 'photo']

class DeleteUser(forms.ModelForm):
    class Meta:
        model = ProfileUser
        fields = []