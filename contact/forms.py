from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["price"].required = False

    full_name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Full name'}),
    )

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Email'}),
    )
    
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Subject'}),
    )
    phone_number = forms.CharField(
        label='Phone Number',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Phone Number'}),
    )
    message = forms.CharField(
        label='Write a message to send',
        help_text='Include all messages what you want to say',
        widget= forms.Textarea(attrs={"class": "shadow form-control"})
    )

    class Meta:
        model = Contact
        fields = (
            'full_name',
            'email',
            'subject',
            'phone_number',
            'message',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            subject = f'{instance.email} trying to contact you'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email, ]
            send_mail( subject, instance.message, email_from, recipient_list )
            instance.save()
        return instance