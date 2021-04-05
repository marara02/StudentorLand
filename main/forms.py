from .models import Task
from .models import Mentor
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дисциплина вопроса'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш вопрос'
            })

        }


class MentorForm(ModelForm):
    class Meta:
        model = Mentor
        fields = ["name", "email", "telephone", "university", "discipline"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша имя и фамилия'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Адрес электронной почты'
            }),
            "telephone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            "university": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш университет'
            }),
            "discipline": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дисциплина, в котором нуждаетесь ментора'
            })
        }
