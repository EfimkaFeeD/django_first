from django import forms

from feedback.models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["mail", "text"]
        labels = {
            "mail": "Почта",
            "text": "Текст сообщения",
        }
        help_texts = {
            "mail": "Введите свой адрес электронной почты, "
            "на него придет ответ от нашего специалиста",
            "text": "Ваше сообщение нашему специалисту (у него лапки)",
        }
