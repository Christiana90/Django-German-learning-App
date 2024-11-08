# users/forms.py
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

#class CustomUserCreationForm(UserCreationForm):
#email = forms.EmailField(required=True)

#class Meta:
   # model = User
   # fields = ('username', 'email', 'password1', 'password2')


from django import forms

# import GeeksModel from models.py
from .models import Register

# create a Form
class RegisterForm(forms.ModelForm):
    # Additional field for confirming password
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:  #Creat tables from the database and not the form
        model = Register
        fields = ["username", "email", "password"]  # Explicitly list fields

        # Specify password field widget (optional, but commonly done for security)
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")

        return cleaned_data

    