from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name='SignUp'),
    path('sign_in/', SignInView.as_view(), name='SignIn'),
    path('log_out/', LogoutView.as_view(), name='LogOut'),
    path('reset_password', ResetPasswordView.as_view(), name='ResetPassword'),
    path('reset_password_done', ResetPasswordDoneView.as_view(), name='ResetPasswordDone'),
    path('set_new_password/<uidb64>/<token>', SetNewPasswordView.as_view(), name='SetNewPassword'),
    path('change_password/', ChangePasswordView.as_view(), name='ChangePassword'),
    path('profile/', ProfileView.as_view(), name='Profile'),
]
