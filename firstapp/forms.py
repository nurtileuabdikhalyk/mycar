from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ("name", "surname", "email", "text", "image")
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Имя"}),
            "surname": forms.TextInput(attrs={"class": "form-control border", "placeholder": "Фамилия"}),
            "email": forms.EmailInput(attrs={"class": "form-control border", "placeholder": "Email"}),
            "text": forms.Textarea(attrs={"class": "form-control border", "placeholder": "Напишите свое сообщение..."}),

        }
