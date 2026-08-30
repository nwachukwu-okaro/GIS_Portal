from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Profile


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'autofocus': True, 'autocomplete': 'email'}),
    )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('organisation', 'department', 'job_title', 'telephone')
        widgets = {
            field: forms.TextInput(attrs={'class': 'systra-input'})
            for field in fields
        }
