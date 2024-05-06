from django import forms
from App_login.models import UserProfile



class ProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']


