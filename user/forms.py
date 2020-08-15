from django import forms
from .models import UserInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    #password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=['username','email','password']

        """def clean(self):
            data=self.cleaned_data
            password=self.cleaned_data.get('password')
            password2=self.cleaned_data.get('password2')
            if password!=password2:
                raise forms.ValidationError('Password not matching')
            return data"""

class UserInfoForm(forms.ModelForm):
    class Meta():
        model=UserInfo
        fields=['name','phone']

    """def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        if len(phone)<10 and len(phone)>10:
            raise forms.ValidationError("Enter 10 digit phone number")
        return phone  """  
