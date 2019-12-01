from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Create your views here.
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView, FormView

from Exams.forms import ExamsCreateForm, SubjectCreateForm, QuestionCreateForm, AnswerCreateForm, ExamAttemptForm
from Exams.models import Exam, Subject, Question, Answer


class ListExams(LoginRequiredMixin, ListView):
    model = Exam
    template_name = 'Exams/Exam/ListExams.html'


class CreateExam(PermissionRequiredMixin, CreateView):
    model = Exam
    form_class = ExamsCreateForm
    success_url = reverse_lazy('ListExams')
    permission_required = 'Exams.add_exam'
    template_name = 'Exams/Exam/ExamCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.exam_author = self.request.user
        return super(CreateExam, self).form_valid(form)


class SubjectCreate(PermissionRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectCreateForm
    success_url = reverse_lazy('CreateExam')
    permission_required = 'Exams.add_subject'
    template_name = 'Exams/Subject/SubjectCreate.html'


class ExamDetail(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = 'Exams/Exam/ExamDetail.html'

    def get_context_data(self, **kwargs):
        context = super(ExamDetail, self).get_context_data(**kwargs)
        context['questions_list'] = Question.objects.filter(question_exam=self.kwargs['pk'])
        return context


class ExamDelete(PermissionRequiredMixin, DeleteView):
    model = Exam
    permission_required = 'Exams.delete_exam'
    success_url = reverse_lazy('ListExams')
    template_name = 'Exams/Exam/ExamDelete.html'


class ExamUpdate(PermissionRequiredMixin, UpdateView):
    model = Exam
    permission_required = 'Exams.change_exam'
    form_class = ExamsCreateForm
    template_name = 'Exams/Exam/ExamUpdate.html'

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['pk']})


class QuestionCreate(PermissionRequiredMixin, CreateView):
    model = Question
    permission_required = 'Exams.add_question'
    form_class = QuestionCreateForm
    template_name = 'Exams/Question/QuestionCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.question_exam = get_object_or_404(Exam, pk=self.kwargs['exam_id'])
        return super(QuestionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['exam_id']})


class QuestionDelete(PermissionRequiredMixin, DeleteView):
    model = Question
    permission_required = 'Exams.delete_question'
    template_name = 'Exams/Question/QuestionDelete.html'

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['exam_id']})


class QuestionUpdate(PermissionRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionCreateForm
    template_name = 'Exams/Question/QuestionUpdate.html'
    permission_required = 'Exam.change_question'

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['exam_id']})


class QuestionDetail(PermissionRequiredMixin, DetailView):
    model = Question
    template_name = 'Exams/Question/QuestionDetail.html'
    permission_required = 'Exams.view_question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['answers_list'] = Answer.objects.filter(answer_question=self.kwargs['pk'])
        return context


class AnswerCreate(PermissionRequiredMixin, CreateView):
    model = Answer
    form_class = AnswerCreateForm
    permission_required = 'Exams.add_answer'
    template_name = 'Exams/Answer/AnswerCreate.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.answer_question = Question.objects.get(pk=self.kwargs['question_id'])
        return super(AnswerCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('QuestionDetail', kwargs={'pk': self.kwargs['question_id']})


class AnswerUpdate(PermissionRequiredMixin, UpdateView):
    model = Answer
    form_class = AnswerCreateForm
    permission_required = 'Exams.change_answer'
    template_name = 'Exams/Answer/AnswerUpdate.html'

    def get_success_url(self):
        return reverse_lazy('QuestionDetail', kwargs={'pk': self.kwargs['question_id']})


class AnswerDelete(PermissionRequiredMixin, DeleteView):
    model = Answer
    permission_required = 'Exams.delete_answer'
    template_name = 'Exams/Answer/AnswerDelete.html'

    def get_success_url(self):
        return reverse_lazy('QuestionDetail', kwargs={'pk': self.kwargs['question_id']})


class ExamAttempt(FormView):
    form_class = ExamAttemptForm
    template_name = 'Exams/Exam/ExamForm.html'

    def get_success_url(self):
        return reverse_lazy('ExamDetail', kwargs={'pk': self.kwargs['exam_id']})

    def get_form_kwargs(self):
        kwargs = super(ExamAttempt, self).get_form_kwargs()
        kwargs['exam_id'] = self.kwargs['exam_id']
        return kwargs

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ExamAttempt, self).form_valid(form)
