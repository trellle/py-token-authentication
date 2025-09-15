from django.urls import path
from user.views import CreateUserView, LoginUserView, ManageUserView
from rest_framework.authtoken import views

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="get-token"),
    path("login/", views.obtain_auth_token, name="login"),
    path("me/", ManageUserView.as_view(), name="manage")
]

app_name = "user"
