from django import forms
from django.contrib.auth.models import User
from django.conf import settings


# create user creation form

class SignUpForm(forms.ModelForm):
    template_name = settings.FORM_TEMPLATE_NAME

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    # Define the model to be used
    class Meta:
        model = User

        # These fields will be used on the form

        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        

        user = super().save(commit=False)

        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 == password2:
            user.set_password(password1)
            super().save()

            return user


class SignInForm(forms.Form):
    """
    provides the a form for user authentications
    """

    template_name = "accounts/form_template.html"
    error_class = 'errors'

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



