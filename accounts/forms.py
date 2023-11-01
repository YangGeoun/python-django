from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model, password_validation
from django import forms

# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()

        fields = ['username', 'beakjoon_nickname']
        # fields = {'first_name', 'last_name', 'email',}
        labels = {
            'username': '이름',
            'beakjoon_nickname': '백준 닉네임',
        }
        widgets = {
            'username': forms.TextInput(attrs={'style': 'color: black; width: 200px; height: 25px; border-radius: 8px;', 'placeholder': ' Change your name'}),        
            'beakjoon_nickname': forms.TextInput(attrs={'style': 'color: black; width: 200px; height: 25px; border-radius: 8px;', 'placeholder': ' Change your nickname'}),
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'beakjoon_nickname', 'username')

class CustomPasswordChangeForm(PasswordChangeForm):
    # class Meta:
    #     model = get_user_model()
    #     fields = ['new_password1', 'new_password2']
    #     labels = {
    #         'new_password1': '새 비밀번호123123',
    #         'new_password2': '새 비밀번호 (확인)'
    #     }
    #     widgets = {
    #         'new_password1': forms.PasswordInput(attrs={'style': 'color: black;', 'placeholder': ' Change your name'}),
    #         'new_password2': forms.PasswordInput(attrs={'style': 'color: black;', 'placeholder': ' Change your name'})
    #     }
    old_password = forms.CharField(
        label = ("기존 비밀번호 "),
        strip = False,
        widget = forms.PasswordInput(
            attrs= {'style': 'color: black; width: 200px; height: 25px; border-radius: 8px;', 'placeholder': 'Enter your old password', "autocomplete": "current-password", "autofocus": True}
        ),
    )

    new_password1 = forms.CharField(
    label = ("새 비밀번호 "),
    widget=forms.PasswordInput(attrs={'style': 'color: black; width: 200px; height: 25px; border-radius: 8px;', 'placeholder': 'Change your password', "autocomplete": "new-password"}),
    strip = False,
    help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label = ("새 비밀번호 (확인) "),
        strip = False,
        widget = forms.PasswordInput(attrs={'style': 'color: black; width: 200px; height: 25px; border-radius: 8px;', 'placeholder': 'Check your new password', "autocomplete": "new-password"}),
    )