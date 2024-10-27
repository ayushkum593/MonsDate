# dating_app/forms.py
from django import forms


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=18)
    gender = forms.ChoiceField(choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ])
    bio = forms.CharField(widget=forms.Textarea)
    interests = forms.CharField(widget=forms.Textarea)
    location = forms.CharField(max_length=100)
    profile_picture = forms.ImageField(required=False)
