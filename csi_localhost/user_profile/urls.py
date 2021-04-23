from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    ProfileView,
    LeaderView
, LogoutView
)

app_name = "user_profile"
urlpatterns = [
    path("profile/", view=login_required(ProfileView.as_view()), name="redirect"),
    path("logout/", view=login_required(LogoutView.as_view()), name="logout"),
    path("leaderboard/", view=LeaderView.as_view(), name="lead"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
