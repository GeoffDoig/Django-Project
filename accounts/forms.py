from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile


class UserLoginForm(forms.Form):
    """
    Form to log users in
    """
    username = forms.CharField(widget=forms.TextInput
                               (attrs={"placeholder": "Email Address"}))
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Form to register users
    """
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # Email Validation
    def clean_email(self):
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get("username")
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u"Email address must be unique")
        return email

    # Password Validation
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if not password1 or not password2:
            raise ValidationError(u"Please confirm your password")
        if password1 != password2:
            raise ValidationError(u"Passwords must match!")
        return password2


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for users to update profile details
    """
    class Meta:
        model = UserProfile
        fields = ["full_name", "street_address1", "street_address2",
                  "town_or_city", "county", "country", "postcode",
                  "phone_number", "avatar"]
