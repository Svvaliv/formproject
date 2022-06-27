from django import forms

from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=20, min_length=2, label="Имя", error_messages={
#         "max_length": "Имя не должно превышать 20 символов",
#         "min_length": "Имя должно содержать по крайней мере 2 символа",
#         "required": "Имя не должно быть пустым",
#     })
#     surname = forms.CharField(max_length=20, min_length=2, label="Фамилия")
#     feedback = forms.CharField(label="Отзыв", widget=forms.Textarea(attrs={
#         "rows": 2,
#         "cols": 20
#     }))
#     rating = forms.IntegerField(label="Рейтинг", min_value=1, max_value=5)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
        labels = {
            "name": "Имя",
            "surname": "Фамилия",
            "feedback": "Отзыв",
            "rating": "Рейтинг"
        }
        error_messages = {
            "name": {
                "max_length": "Имя не должно превышать 20 символов",
                "min_length": "Имя должно содержать по крайней мере 2 символа",
                "required": "Имя не должно быть пустым",
            },
            "surname": {
                "max_length": "Фамилия не должна превышать 20 символов",
                "min_length": "Фамилия должна содержать по крайней мере 2 символа",
                "required": "Фамилия не должна быть пустой",
            },
            "feedback": {
                "required": "Отзыв не может быть пустым",
            },
            "rating": {
                "required": "Рейтинг должен быть от 1 до 5",
            }
        }
