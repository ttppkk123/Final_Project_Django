from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    model = ContactMessage
    fields = ['name', 'email', 'subject', 'message']
