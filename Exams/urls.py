from django.urls import path
from .views import *

urlpatterns = [
    path('exams_list/', ListExams.as_view(), name='ListExams'),
    path('exam_create/', CreateExam.as_view(), name='CreateExam'),
    path('subject_create/', SubjectCreate.as_view(), name='SubjectCreate'),
    path('exam_detail/<pk>', ExamDetail.as_view(), name='ExamDetail'),
    path('exam_delete/<pk>', ExamDelete.as_view(), name='ExamDelete'),
    path('exam_update/<pk>', ExamUpdate.as_view(), name='ExamUpdate'),
]
