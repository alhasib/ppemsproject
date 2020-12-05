
from django import forms
from django.contrib.auth.models import User, Group
from .models import *

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group col-md-3  bg-light'}))
#     roll = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control bg-light'}), queryset=Group.objects.all())
#     role = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-group col-lg-3 form_field',}), queryset=Group.objects.all())

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'username', 'password', 'roll']

#         help_texts = {
#             'username': None,
#             'email': None,
#         }

#         widgets = {
#             'first_name':forms.TextInput(attrs={'class':'form-control bg-light form_field', 'placeholder':"Enter First Name..."}),
#             'last_name':forms.TextInput(attrs={'class':'form-control bg-light form_field', 'placeholder':"Enter Last Name..."}),
#             'username':forms.TextInput(attrs={'class':'form-group col-md-3 bg-light form_field', 'placeholder':"Enter User Name..."}),
#             'email':forms.TextInput(attrs={'class':'form-control bg-light form_field', 'placeholder':'Enter Your Email Address ..'}),
#         }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-field form-group mt-3 col-md-3 bg-light', 'placeholder':"Enter Password..."}))
    role = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-group col-md-3 form_field',}), queryset=Group.objects.all())
    department = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-field form-group col-md-4 form_field',}), queryset=Department.objects.all())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'role', 'email', 'department']
        help_texts = {
            # 'username': "Emtr dmoief class:btn btn-primary",
            'username':None,
            'email': None,
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control bg-light form-field', 'placeholder':"Enter First Name..."}),
            'last_name':forms.TextInput(attrs={'class':'form-control bg-light form-field', 'placeholder':"Enter Last Name..."}),
            'username':forms.TextInput(attrs={'class':'form-group col-md-3 bg-light form-field', 'placeholder':"Enter User Name..."}),
            'email':forms.TextInput(attrs={'class':'form-group col-md-5 bg-light form-field', 'placeholder':'Enter Your Email Address ..'}),

        }



class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-6 bg-light'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 bg-light', 'placeholder':"Enter Password..."}))


class DailyTaskForm(forms.ModelForm):
    class Meta:
        model = DailyTask

        fields = '__all__'
        exclude = ['date', 'user']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'})
        }


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ['from_date', 'to_date', 'cause_of_leave']
        # exclude = ['user', 'status', 'checked_in']

        widgets = {
            'from_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control datepicker'}),
            'to_date':forms.DateInput(attrs={'type': 'date', 'class':'form-control datepicker'}),
            'cause_of_leave':forms.Textarea(attrs={'class':'form-control'})
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']