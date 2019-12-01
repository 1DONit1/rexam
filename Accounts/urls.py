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
    path('user_list/', UserList.as_view(), name='UserList'),
    path('user_update/<pk>', ProfileUpdate.as_view(), name='ProfileUpdate'),
    path('user_delete/<pk>', ProfileDelete.as_view(), name='ProfileDelete'),
    path('study_group_create/', StudyGroupCreate.as_view(), name='StudyGroupCreate'),
    path('study_group_update/<pk>', StudyGroupUpdate.as_view(), name='StudyGroupUpdate'),
    path('study_group_delete/<pk>', StudyGroupDelete.as_view(), name='StudyGroupDelete'),
    path('study_group_list/', StudyGroupList.as_view(), name='StudyGroupList'),
]
