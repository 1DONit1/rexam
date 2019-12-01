from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import safe

from Exams.models import Exam, Subject, Question, Answer


class ExamsCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ('exam_subject', 'exam_header', 'exam_description')
        widgets = {
            'exam_header': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'exam_description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание'}),
            'exam_subject': Select(attrs={'class': 'form-control col-5 d-inline', 'placeholder': 'Предмет'})
        }


class SubjectCreateForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя предмета'})
        }


class QuestionCreateForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['question_exam']
        widgets = {
            'question_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст вопроса'}),
        }


class AnswerCreateForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ['answer_question']
        widgets = {
            'answer_text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст ответа'}),
        }


class ExamAttemptForm(forms.Form):
    def __init__(self, *args, **kwargs):
        attempted_exam = get_object_or_404(Exam, pk=kwargs.pop('exam_id', None))
        questions = attempted_exam.get_question_set()
        super(ExamAttemptForm, self).__init__(*args, **kwargs)
        for question in questions:
            choices = []
            answers_set = question.get_answers_set()
            question_label = question.question_text
            if question.question_image:
                question_label += safe(
                    '<a target="_blank" rel="noopener noreferrer" href="' + question.question_image.url + '"><img class="d-block img-thumbnail rounded" width="500px" height="500px" src="' +
                    question.question_image.url + '"/></a>')
            for answer in answers_set:
                answer_choice = answer.answer_text
                if answer.answer_image:
                    answer_choice += '<a target="_blank" rel="noopener noreferrer" href="' + answer.answer_image.url + '"><img class="d-block img-thumbnail rounded" width="300px" height="300px" src="' + answer.answer_image.url + '"/></a>'

                choices.append((answer.pk, safe(answer_choice)))
            self.fields['question_%d' % question.pk] = forms.MultipleChoiceField(label=question_label,
                                                                                 required=True,
                                                                                 choices=choices,
                                                                                 widget=forms.CheckboxSelectMultiple)
