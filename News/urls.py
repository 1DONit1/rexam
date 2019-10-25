from django.urls import path
from .views import *

urlpatterns = [
    path('news_create/', NewsCreate.as_view(), name='CreateNews'),
    path('category_create', CategoryCreate.as_view(), name='CreateCategory'),
    path('news_remove/<pk>', RemoveNews.as_view(), name='RemoveNews'),
    path('news_update/<pk>', UpdateNews.as_view(), name='UpdateNews'),
    path('', ListNews.as_view(), name='ListNews'),
]
