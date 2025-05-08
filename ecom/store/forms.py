from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Form for user registration
class UserRegistrationForm(forms.ModelForm):
    # Password and confirm password fields
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    # Meta class for mapping the form to the User model
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    # Validate that password and confirm password match
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

# Form for user login
class LoginForm(forms.Form):
    # Fields for username and password
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    # Custom validation to authenticate the user
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # Try to authenticate the user with the provided credentials
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid username or password")
            # Attach the user object to the cleaned data
            cleaned_data['user'] = user
        return cleaned_data
