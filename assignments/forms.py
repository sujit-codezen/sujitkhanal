from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Assignment
from django.conf import settings
from django.core.mail import send_mail
from taggit.forms import TagWidget

ASSIGNMENT_PRIORITY_CHOICES = (
        ("Urgent", "Urgent"),
        ("Medium", "Medium"),
        ("With In 15 Days", "With In 15 Days"),
        ("With In 1 month", "With In 1 month"),
    )

ASSIGNMENT_STATUS_CHOICES = (
    ("Pending", "Pending"),
    ("Working On", "Working On"),
    ("Delivered", "Delivered"),
)

class AssignmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["price"].required = False
        self.fields['assignment_description'].widget.attrs['cols'] = 70
        self.fields['assignment_description'].widget.attrs['rows'] = 2

    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Email'}),
    )

    name = forms.CharField(
        label='Full Name',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Full Name'}),
    )

    assignment_title = forms.CharField(
        label='Assignment Title',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Assignment Tilte'}),
    )
    assignment_description = forms.CharField(
        label='Assignment Description',
        help_text='Include all description and can upload image too',
        widget= forms.Textarea(attrs={"class": "shadow form-control"})
    )
    assignment_priority = forms.ChoiceField(
        choices = ASSIGNMENT_PRIORITY_CHOICES,
        label='Assignment Priority',
        widget=forms.Select(attrs={'class': 'shadow form-control', 'placeholder': 'Assignment Priority'}),
    )
    contact_no = forms.CharField(
        label='Contact no',
        widget=forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Contact No'}),
    )
    file = forms.FileField(
        label='File',
        help_text='Upload PDF file',
        widget=forms.FileInput(attrs={'class': 'shadow form-control'}),
    )

    language_used = forms.CharField(
        label='Language to used',
        help_text='Seperate language by comma like (python, django)',
        widget = TagWidget(
        attrs={'data-role':'tagsinput','placeholder':'Add language to be used','class':'shadow form-control', }),
    )

    date_up_to = forms.DateTimeField(
        label= 'Deadline',
        widget= forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'shadow form-control'})
    )

    class Meta:
        model = Assignment
        fields = (
            'name',
            'email',
            'contact_no',
            'assignment_title',
            'assignment_description',
            'assignment_priority',
            'file',
            'language_used',
            'date_up_to',
        )

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.assignment_priority == "Urgent":
            instance.price = instance.price + 40
        elif instance.assignment_priority == "Medium":
            instance.price = instance.price + 20
        else:
            instance.price = instance.price
        if commit:
            subject1 = f'New Assignment of {instance.assignment_title}'
            subject2 = f'Submission of Assignment'
            message1 = f'New assignment arrived check on admin panel'
            message2 = f'Hi {instance.name}, Your assignment has been requested successfully. We will contact you soon'
            email_from = settings.EMAIL_HOST_USER
            recipient_list1 = [settings.EMAIL_HOST_USER, ]
            recipient_list2 = [instance.email, ]
            send_mail( subject1, message1, email_from, recipient_list1 )
            send_mail( subject2, message2, email_from, recipient_list2 )
            instance.save()
        return instance