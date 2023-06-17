from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Rating


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ratingForm(ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs = {'class': 'materialize-textarea'}), required=False)
    # rating = forms.ChoiceField(widget=forms.Select(), required=True)
    class Meta:
        model = Rating
        fields = [ 'description', 'rating']