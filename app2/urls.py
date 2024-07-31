from django.urls import path
from .views import student_registration, save_student, export_students_csv, export_students_pdf

urlpatterns = [
    path('register/', student_registration, name='student_registration'),
    path('save_student/', save_student, name='save_student'),
    path('export/csv/', export_students_csv, name='export_students_csv'),
    path('export/pdf/', export_students_pdf, name='export_students_pdf'),
]
