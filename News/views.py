from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from News.forms import NewsCreateForm, CategoryCreateForm
from News.models import News, NewsCategory


class NewsCreate(PermissionRequiredMixin, CreateView):
    model = News
    success_url = reverse_lazy('HomePage')
    permission_required = 'News.add_news'
    form_class = NewsCreateForm
    template_name = 'News/NewsCreate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.news_author = self.request.user
        return super(NewsCreate, self).form_valid(form)


class CategoryCreate(PermissionRequiredMixin, CreateView):
    model = NewsCategory
    success_url = reverse_lazy('CreateNews')
    template_name = 'News/CategoryCreate.html'
    permission_required = 'News.add_newscategory'
    form_class = CategoryCreateForm


class RemoveNews(PermissionRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy('HomePage')
    permission_required = 'News.delete_news'
    template_name = 'News/NewsRemove.html'


class UpdateNews(PermissionRequiredMixin, UpdateView):
    model = News
    success_url = reverse_lazy('HomePage')
    permission_required = 'News.change_news'
    form_class = NewsCreateForm
    template_name = 'News/UpdateNews.html'


class ListNews(LoginRequiredMixin, ListView):
    model = News
    template_name = 'News/ListNews.html'
    paginate_by = 4
