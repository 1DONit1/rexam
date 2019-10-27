from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from Exams.forms import ExamsCreateForm, SubjectCreateForm, QuestionCreateForm
from Exams.models import Exam, Subject, Question


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
        context['questions_list'] = Question.objects.filter(question_exam=self.kwargs['pk'])
        return context


class ExamDelete(PermissionRequiredMixin, DeleteView):
    model = Exam
    permission_required = 'Exams.delete_exam'
    success_url = reverse_lazy('ListExams')
    template_name = 'Exams/ExamDelete.html'


class ExamUpdate(PermissionRequiredMixin, UpdateView):
    model = Exam
    permission_required = 'Exams.change_exam'
    form_class = ExamsCreateForm
    template_name = 'Exams/ExamUpdate.html'

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['pk']})


class QuestionCreate(PermissionRequiredMixin, CreateView):
    model = Question
    permission_required = 'Exam.add_question'
    form_class = QuestionCreateForm
    template_name = 'Exams/QuestionCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.question_exam = Exam.objects.get(pk=self.kwargs['exam_id'])
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['exam_id']})
