from django.urls import re_path

from users.views.sign_up_view import SignUpView

urlpatterns = [
    re_path(r"sign_up",SignUpView.as_view()),
    ]