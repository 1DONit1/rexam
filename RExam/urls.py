from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.views.generic import RedirectView

from RExam import settings
from .views import AboutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('Accounts.urls')),
    path('news/', include('News.urls')),
    path('', RedirectView.as_view(permanent=False, url='news/'), name='HomePage'),
    path('about/', AboutPage.as_view(), name='AboutPage'),
    path('exams/', include('Exams.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
