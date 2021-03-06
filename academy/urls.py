from django.urls import path
from .views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('trainer/', TrainerListView.as_view(), name='trainer-list'),
    path('trainer/<int:pk>/', TrainerDetailView.as_view(), name='trainer-detail'),
    path('trainer/create/', create_trainer, name='trainer-create'),
    path('trainer/<int:pk>/update/', update_trainer, name='trainer-update'),
    path('trainer/<int:pk>/delete/', TrainerDelete.as_view(), name='trainer-delete'),
    path('student/personal/', student_personal_view, name='student-personal'),
    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('student/create/', create_student, name='student-create'),
    path('student/<int:pk>/update/', update_student, name='student-update'),
    path('student/<int:pk>/delete/', StudentDelete.as_view(), name='student-delete'),
    path('privilege/', PrivilegeListView.as_view(), name='privilege-list'),
    path('privilege/<int:pk>/', PrivilegeDetailView.as_view(), name='privilege-detail'),
    path('privilege/create/', PrivilegeCreate.as_view(), name='privilege-create'),
    path('privilege/<int:pk>/update/', PrivilegeUpdate.as_view(), name='privilege-update'),
    path('privilege/<int:pk>/delete/', PrivilegeDelete.as_view(), name='privilege-delete'),
    path('section/', SectionListView.as_view(), name='section-list'),
    path('section/<int:pk>/', SectionDetailView.as_view(), name='section-detail'),
    path('section/create/', SectionCreate.as_view(), name='section-create'),
    path('section/<int:pk>/update/', SectionUpdate.as_view(), name='section-update'),
    path('section/<int:pk>/delete/', SectionDelete.as_view(), name='section-delete'),
    path('training/', TrainingListView.as_view(), name='training-list'),
    path('training/<int:pk>/', TrainingDetailView.as_view(), name='training-detail'),
    path('training/create/', TrainingCreate.as_view(), name='training-create'),
    path('training/<int:pk>/update/', TrainingUpdate.as_view(), name='training-update'),
    path('training/<int:pk>/delete/', TrainingDelete.as_view(), name='training-delete'),
    path('event/', EventListView.as_view(), name='event-list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/create/', EventCreate.as_view(), name='event-create'),
    path('event/<int:pk>/update/', EventUpdate.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDelete.as_view(), name='event-delete'),
    path('carnet/', CarnetListView.as_view(), name='carnet-list'),
    path('carnet/<int:pk>/', CarnetDetailView.as_view(), name='carnet-detail'),
    path('carnet/create/', CarnetCreate.as_view(), name='carnet-create'),
    path('carnet/<int:pk>/update/', CarnetUpdate.as_view(), name='carnet-update'),
    path('carnet/<int:pk>/delete/', CarnetDelete.as_view(), name='carnet-delete'),
    path('exam/', ExamListView.as_view(), name='exam-list'),
    path('exam/<int:pk>/', ExamDetailView.as_view(), name='exam-detail'),
    path('exam/create/', ExamCreate.as_view(), name='exam-create'),
    path('exam/<int:pk>/update/', ExamUpdate.as_view(), name='exam-update'),
    path('exam/<int:pk>/delete/', ExamDelete.as_view(), name='exam-delete'),
]

