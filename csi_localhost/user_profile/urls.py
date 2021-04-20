from django.urls import path

from .views import (
    profile_view
    ,leader_view
    ,logout
)

app_name = "user_profile"
urlpatterns = [
    path("profile/", view=profile_view, name="redirect"),
    path("logout/", view=logout, name="logout"),
    path("leaderboard/", view=leader_view, name="lead"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
