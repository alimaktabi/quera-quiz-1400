from django import forms


class SignUpForm(forms.Form):
    name = forms.CharField(max_length=225, required=False)

    email = forms.EmailField(required=True)

    password = forms.CharField(required=True)


class LoginForm(forms.Form):

    email = forms.CharField(required=True)

    password = forms.CharField(required=True)

