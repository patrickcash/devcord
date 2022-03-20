from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Room


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'topic', 'description']