__all__ = ["feedback"]

from django.core.mail import send_mail
from django.shortcuts import redirect, render

from feedback.forms import FeedbackForm
from lyceum.settings import MAIL


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get("mail")
        text = form.cleaned_data.get("text")
        send_mail(
            subject="Ваш FeedBack",
            message=text,
            from_email=MAIL,
            recipient_list=[email],
        )
        return redirect("feedback:feedback")
    return render(request, "feedback/feedback.html", {"form": form})
