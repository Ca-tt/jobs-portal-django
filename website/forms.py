from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Vacancy


class SignupForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm password"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "email")
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Username"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Email address"}
            ),
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "You entered wrong username or password. Please dobuble check and try again.",
        "inactive": "This account is inactive. Please contact support.",
    }


class JobForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = "__all__"
        widgets = {
            "position_title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter job title"}
            ),
            "job_description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Enter job description",
                }
            ),
            "location": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter location"}
            ),
            "salary_from": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Minimum salary"}
            ),
            "salary_to": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "Maximum salary"}
            ),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # print("🐍 File: website/forms.py | Line: 43 | __init__ ~ field_name",field_name)
            if field_name not in ["is_active", "employment_type"]:
                field.widget.attrs["class"] = (
                    field.widget.attrs.get("class", "") + " form-control"
                )
