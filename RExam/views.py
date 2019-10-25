from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from News.models import News


class AboutPage(LoginRequiredMixin, TemplateView):
    template_name = 'RExam/About.html'
