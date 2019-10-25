from django.forms import ModelForm, TextInput, Textarea, Select

from Exams.models import Exam, Subject


class ExamsCreateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ('exam_header', 'exam_description', 'exam_subject')
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
