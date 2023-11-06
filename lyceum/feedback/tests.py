__all__ = ["FeedbackFormTests"]

from django.test import TestCase
from django.urls import reverse

from feedback.forms import FeedbackForm


class FeedbackFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = FeedbackForm()

    def test_form_mail_label(self):
        self.assertEqual(self.form.fields["mail"].label, "Почта")

    def test_form_mail_help_text(self):
        self.assertEqual(
            self.form.fields["mail"].help_text,
            "Введите свой адрес электронной почты, на него придет "
            "ответ от нашего специалиста",
        )

    def test_form_text_label(self):
        self.assertEqual(self.form.fields["text"].label, "Текст сообщения")

    def test_form_text_help_text(self):
        self.assertEqual(
            self.form.fields["text"].help_text,
            "Ваше сообщение нашему специалисту (у него лапки)",
        )

    def test_form_in_context(self):
        response = self.client.get(reverse("feedback:feedback"))
        self.assertIn("form", response.context)

    def test_form_redirect(self):
        response = self.client.post(
            reverse("feedback:feedback"),
            data={
                "mail": "feedbacktest@mail.com",
                "text": "Test text feedback",
            },
            follow=True,
        )
        self.assertRedirects(response, reverse("feedback:feedback"))
