# forms.py
from django import forms
from .models import Subscriber
from django_recaptcha.fields import ReCaptchaField

class SubscriberForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Subscriber
        fields = ['email', 'captcha']
