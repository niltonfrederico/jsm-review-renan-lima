from django.urls import path, include
from users.api.views import UsersListAPIView, UserDetailAPIView, UserCreateView

urlpatterns = [
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:id>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("users/<str:region>/<str:type>/", UsersListAPIView.as_view(), name="users-region-and-type"),
    path("users/<str:region_or_type>/", UsersListAPIView.as_view(), name="users-region-or-type"),
    path("users/", UsersListAPIView.as_view(), name="users-list"),

    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
