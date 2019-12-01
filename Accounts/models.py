from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse


class StudyGroup(models.Model):
    group_name = models.CharField(max_length=10, blank=False, null=False, verbose_name=u'Имя группы')

    def __str__(self):
        return self.group_name

    def get_update_url(self):
        return reverse('StudyGroupUpdate', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('StudyGroupDelete', kwargs={'pk': self.id})

    class Meta:
        verbose_name = u'Учебная группа'
        verbose_name_plural = u'Учебные группы'


class UserAccount(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=False, verbose_name=u'Отчество')
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True, blank=True)

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'

    def get_absolute_url(self):
        return reverse('Profile', kwargs={"pk": self.id})

    def get_update_url(self):
        return reverse('ProfileUpdate', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('ProfileDelete', kwargs={'pk': self.id})
