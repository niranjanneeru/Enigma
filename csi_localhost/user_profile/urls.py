from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    ProfileView,
    leader_view,
    LogoutView,
    ProfileChangeView
)

app_name = "user_profile"
urlpatterns = [
    path("profile/", view=login_required(ProfileView.as_view()), name="redirect"),
    path("profile_change/", view=login_required(ProfileChangeView.as_view()), name="profile_change"),
    path("logout/", view=login_required(LogoutView.as_view()), name="logout"),
    path("leaderboard/", view=leader_view, name="lead"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
