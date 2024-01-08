from django import forms

from main.models import ContactMessage


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ("full_name", "email", "message")