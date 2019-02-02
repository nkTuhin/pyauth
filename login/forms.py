from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# register form class


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'user_name',
               'placeholder': 'User name | e.g. Tuhin', 'required': 'required'}
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'password',
               'placeholder': 'Enter password | e.g. 3xc9g4Sv33e',
               'required': 'required'}
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'confirm_password',
               'placeholder': 'Confirm your password',
               'required': 'required'}
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'id': 'user_email',
               'placeholder': 'Example: YourEmail@example.com',
               'required': 'required'}
    ))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


# login form class

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'id': 'user_name',
               'placeholder': 'Authenticate user name', 'required': 'required'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'id': 'user_password',
               'placeholder': 'Authenticate user name',
               'required': 'required'}
    ))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
                if not user.check_password(password):
                    raise forms.ValidationError("Incorrect passwprd")
                if not user.is_active:
                    raise forms.ValidationError("The user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
