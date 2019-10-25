from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from Exams.forms import ExamsCreateForm, SubjectCreateForm
from Exams.models import Exam, Subject


class ListExams(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'Exams/ListExams.html'


class CreateExam(PermissionRequiredMixin, CreateView):
    model = Exam
    form_class = ExamsCreateForm
    success_url = reverse_lazy('ListExams')
    permission_required = 'Exams.add_exam'
    template_name = 'Exams/ExamCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.exam_author = self.request.user
        return super(CreateExam, self).form_valid(form)


class SubjectCreate(PermissionRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectCreateForm
    success_url = reverse_lazy('CreateExam')
    permission_required = 'Exams.add_subject'
    template_name = 'Exams/SubjectCreate.html'


class ExamDetail(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = 'Exams/ExamDetail.html'

    def get_context_data(self, **kwargs):
        context = super(ExamDetail, self).get_context_data(**kwargs)
        context['question_count'] = "TODO"
        return context
