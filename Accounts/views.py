from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, LoginView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, RedirectView, TemplateView, UpdateView, ListView

from Accounts.forms import SignUpForm, SignInForm, ResetPasswordForm, PasswordSetForm, ChangePasswordForm, \
    UserProfileForm
from Accounts.models import UserAccount
from RExam.mixins import NotAuthCheckMixin


class SignUpView(NotAuthCheckMixin, CreateView):
    back_page = reverse_lazy('ListNews')
    form_class = SignUpForm
    success_url = reverse_lazy('SignIn')
    template_name = 'Accounts/SignUp.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SignUpView, self).dispatch(request, *args, **kwargs)


class SignInView(NotAuthCheckMixin, LoginView):
    form_class = SignInForm
    back_page = reverse_lazy('ListNews')
    template_name = 'Accounts/SignIn.html'

    def get_success_url(self):
        return reverse_lazy('ListNews')


class LogoutView(LoginRequiredMixin, RedirectView):
    url = reverse_lazy('SignIn')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ResetPasswordView(NotAuthCheckMixin, PasswordResetView):
    form_class = ResetPasswordForm
    success_url = reverse_lazy('ResetPasswordDone')
    template_name = 'Accounts/ResetPassword.html'
    email_template_name = 'Accounts/ResetPasswordEmail.html'
    subject_template_name = 'Accounts/ResetPasswordSubject.txt'


class ResetPasswordDoneView(NotAuthCheckMixin, TemplateView):
    template_name = 'Accounts/ResetPasswordDone.html'


class SetNewPasswordView(NotAuthCheckMixin, PasswordResetConfirmView):
    form_class = PasswordSetForm
    success_url = reverse_lazy('SignIn')
    template_name = 'Accounts/SetNewPassword.html'


class ChangePasswordView(PasswordChangeView):
    success_url = reverse_lazy('LogOut')
    form_class = ChangePasswordForm
    template_name = 'Accounts/ChangePassword.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'Accounts/Profile.html'
    form_class = UserProfileForm
    model = UserAccount

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('Profile')

    def form_valid(self, form):
        if self.request.user != self.get_object():
            raise PermissionDenied
        post = form.save(commit=False)
        post.username = self.request.user.username
        post.save()
        return super(ProfileView, self).form_valid(form)


class UserList(PermissionRequiredMixin, ListView):
    model = UserAccount
    permission_required = 'Accounts.view_useraccount'
    template_name = 'Accounts/UserList.html'


