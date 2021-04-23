from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    QuestionView
)

app_name = "game"
urlpatterns = [
    path("next/", view=login_required(QuestionView.as_view()), name="quiz"),
]
