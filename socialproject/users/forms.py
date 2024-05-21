from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo"]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    # 因為想在password自己設定名稱
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    # 想直接使用預設的就在field裡面
    class Meta:
        model = User
        fields = ["username", "email"]

    def check_password(self):
        if self.cleaned_data["password"] != self.cleaned_data["password_confirm"]:
            raise forms.ValidationError("Passwords do not match")
        return self.cleaned_data["password"]