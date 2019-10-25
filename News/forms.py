from django.forms import ModelForm, TextInput, Textarea, Select

from News.models import News, NewsCategory


class NewsCreateForm(ModelForm):
    class Meta:
        model = News
        fields = ('news_header', 'news_content', 'news_category')
        widgets = {
            'news_header': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок'}),
            'news_content': Textarea(attrs={'class': 'form-control', 'placeholder': 'Содержание'}),
            'news_category': Select(attrs={'class': 'form-control col-5 d-inline', 'placeholder': 'Категория'})
        }


class CategoryCreateForm(ModelForm):
    class Meta:
        model = NewsCategory
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя категории'})
        }
