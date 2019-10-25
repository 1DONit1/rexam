from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class NotAuthCheckMixin(AccessMixin):
    back_page = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.back_page)
        return super(NotAuthCheckMixin, self).dispatch(request, *args, **kwargs)
