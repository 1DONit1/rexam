from django.urls import path
from .views import *

urlpatterns = [
    path('exams_list/', ListExams.as_view(), name='ListExams'),
    path('exam_create/', CreateExam.as_view(), name='CreateExam'),
    path('subject_create/', SubjectCreate.as_view(), name='SubjectCreate'),
    path('exam_detail/<pk>', ExamDetail.as_view(), name='ExamDetail'),
    path('exam_delete/<pk>', ExamDelete.as_view(), name='ExamDelete'),
    path('exam_update/<pk>', ExamUpdate.as_view(), name='ExamUpdate'),
    path('question_create/<int:exam_id>', QuestionCreate.as_view(), name='QuestionCreate'),
    path('question_delete/<pk>/<int:exam_id>', QuestionDelete.as_view(), name='QuestionDelete'),
    path('question_update/<pk>/<int:exam_id>', QuestionUpdate.as_view(), name='QuestionUpdate'),
    path('question_detail/<pk>', QuestionDetail.as_view(), name='QuestionDetail'),
    path('answer_create/<int:question_id>', AnswerCreate.as_view(), name='AnswerCreate'),
    path('answer_update/<pk>/<int:question_id>', AnswerUpdate.as_view(), name='AnswerUpdate'),
    path('answer_delete/<pk>/<int:question_id>', AnswerDelete.as_view(), name='AnswerDelete'),
    path('exam_start/<int:exam_id>', ExamAttempt.as_view(), name='ExamStart'),
    path('subject_list/', SubjectList.as_view(), name='SubjectList'),
    path('subject_update/<pk>', SubjectUpdate.as_view(), name='SubjectUpdate'),
    path('subject_delete/<pk>', SubjectDelete.as_view(), name='SubjectDelete'),
]
