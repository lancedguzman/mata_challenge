from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    """Creates the Contact Form."""
    class Meta:
        model = Contact
        fields = ["subject", "email",
                  "message",]