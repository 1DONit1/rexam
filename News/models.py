# Create your models here.
from django.db.models import Model, CharField, TextField, ImageField, DateTimeField, ForeignKey, SET_NULL
from django.urls import reverse

from Accounts.models import UserAccount


class NewsCategory(Model):
    name = CharField(max_length=20, null=False, blank=False, verbose_name=u'Имя категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = u'Категории'
        verbose_name = u'Категория'


class News(Model):
    news_header = CharField(max_length=50, null=False, blank=False, verbose_name=u'Заголовок новости')
    news_content = TextField(null=False, blank=False, verbose_name=u'Содержание новости')
    news_category = ForeignKey(NewsCategory, null=True, blank=False, on_delete=SET_NULL,
                               verbose_name=u'Категория новости')
    news_date = DateTimeField(auto_now_add=True, blank=False, verbose_name=u'Дата и время новости')
    news_author = ForeignKey(UserAccount, null=True, on_delete=SET_NULL, verbose_name=u'Автор новости')

    def __str__(self):
        return self.news_header

    def get_update_url(self):
        return reverse('UpdateNews', kwargs={'pk': self.id})

    def get_remove_url(self):
        return reverse('RemoveNews', kwargs={'pk': self.id})

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
