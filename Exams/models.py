from django.db.models import Model, CharField, TextField, DateField, ForeignKey, SET_NULL
from django.urls import reverse

from Accounts.models import UserAccount


class Subject(Model):
    name = CharField(max_length=30, blank=False, null=False, verbose_name=u'Имя предмета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Exam(Model):
    exam_header = CharField(max_length=30, blank=False, null=False, verbose_name=u'Заголовок экзамена')
    exam_description = TextField(blank=False, null=True, verbose_name=u'Описание экзамена')
    exam_date = DateField(auto_now_add=True, blank=False, null=True, verbose_name=u'Дата создания')
    exam_subject = ForeignKey(Subject, blank=False, null=True, on_delete=SET_NULL, verbose_name=u'Предмет')
    exam_author = ForeignKey(UserAccount, blank=False, null=True, on_delete=SET_NULL, verbose_name=u'Автор')

    def __str__(self):
        return self.exam_header

    def get_detail_url(self):
        return reverse('ExamDetail', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('ExamDelete', kwargs={'pk': self.id})

    class Meta:
        verbose_name = u'Экзамен'
        verbose_name_plural = u'Экзамены'
