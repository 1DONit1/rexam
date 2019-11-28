from django.db.models import Model, CharField, TextField, DateField, ForeignKey, SET_NULL, CASCADE, ImageField, \
    BooleanField
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

    def get_update_url(self):
        return reverse('ExamUpdate', kwargs={'pk': self.id})

    def get_add_question_url(self):
        return reverse('QuestionCreate', kwargs={'exam_id': self.id})

    def get_start_url(self):
        return reverse('ExamStart', kwargs={'exam_id': self.id})

    class Meta:
        verbose_name = u'Экзамен'
        verbose_name_plural = u'Экзамены'


class Question(Model):
    question_text = TextField(blank=False, null=False, verbose_name=u'Текст вопроса')
    question_exam = ForeignKey(Exam, blank=False, null=False, on_delete=CASCADE, verbose_name=u'Вопрос к экзамену')
    question_image = ImageField(upload_to='question_images', blank=True, null=True, verbose_name=u'Изображение вопроса')

    def __str__(self):
        return self.question_text

    def get_detail_url(self):
        return reverse('QuestionDetail', kwargs={'pk': self.id})

    def get_add_answer_url(self):
        return reverse('AnswerCreate', kwargs={'question_id': self.id})

    def get_delete_url(self):
        return reverse('QuestionDelete', kwargs={'pk': self.id, 'exam_id': self.question_exam.id})

    def get_update_url(self):
        return reverse('QuestionUpdate', kwargs={'pk': self.id, 'exam_id': self.question_exam.id})

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'
        db_table = 'exam_questions'


class Answer(Model):
    answer_text = TextField(blank=False, null=False, verbose_name=u'Текст ответа')
    answer_question = ForeignKey(Question, blank=False, null=False, on_delete=CASCADE, verbose_name=u'Ответ к вопросу')
    answer_image = ImageField(upload_to='answer_images', blank=True, null=True, verbose_name=u'Изображение ответа')
    answer_truth = BooleanField(blank=False, null=False, verbose_name=u'Правильный ответ?')

    def get_delete_url(self):
        return reverse('AnswerDelete', kwargs={'pk': self.id, 'question_id': self.answer_question.id})

    def get_update_url(self):
        return reverse('AnswerUpdate', kwargs={'pk': self.id, 'question_id': self.answer_question.id})

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
        db_table = 'exam_answers'
