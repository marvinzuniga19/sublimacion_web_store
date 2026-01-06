from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Formulario de contacto"""
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu nombre completo'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'tu@email.com'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Tu teléfono (opcional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Asunto de tu mensaje'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Escribe tu mensaje aquí...',
                'rows': 5
            }),
        }
