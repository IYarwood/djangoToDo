from django import forms
from django.contrib.auth.models import User
from .models import Task
from django.core.exceptions import ValidationError

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['priority', 'task_name',  'dueDate']

class newUserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email"]

    def checkPass(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

    def checkUsername(self):
        userModel = User
        users = User.objects.get(username=self.cleaned_data.get('username'))

        if len(users) > 0:
            raise ValidationError("Username in use")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user