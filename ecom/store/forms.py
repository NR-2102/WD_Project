from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Password field with hidden input
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)  # Password confirmation field

    class Meta:
        model = User  # Use Django's built-in User model
        fields = ('username', 'first_name', 'email')  # Fields to include in the form

    def clean_password2(self):
        cd = self.cleaned_data  # Get cleaned data from the form
        if cd['password'] != cd['password2']:  # Ensure passwords match
            raise forms.ValidationError('Passwords don\'t match.')  # Raise error if they don't match
        return cd['password2']

# Login Form
class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

    def clean(self):
        cleaned_data = super().clean()  # Call parent class's clean method
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)  # Authenticate user
            if not user:
                raise forms.ValidationError("Invalid username or password")  # Raise error if authentication fails
            cleaned_data['user'] = user  # Attach the user to the cleaned data
        return cleaned_data
