from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee

class SignUpForm(UserCreationForm):
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
    position = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Position'}),
        required=False
    )
    salary = forms.IntegerField(
        label="",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salary'}),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Username',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm Password',
        })

class AddRecordForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),label="Your name")
    position = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Your Position", "class":"form-control"}),label="Your position")
    salary = forms.IntegerField(required=True,widget=forms.NumberInput(attrs={"placeholder": "Your Salary","class": "form-control"}),label="Salary")

    class Meta:
        model = Employee
        fields = ['name', 'position', 'salary']