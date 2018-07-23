from django.urls import path

from . import views

app_name = 'college'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/course/', views.CourseView.as_view(), name='course'),
    path('<int:pk>/department/', views.DepartmentView.as_view(), name='department'),
    path('<int:pk>/year/', views.SemesterView.as_view(), name='year'),
    path('<int:pk>/subject/', views.SubjectView.as_view(), name='subject'),
    path('add/', views.CollegeCreate.as_view(), name='college_add'),
    path('add_course/', views.CourseCreate.as_view(), name='course_add'),
    path('add_department/', views.DepartmentCreate.as_view(), name='department_add'),
    path('add_semester/', views.SemesterCreate.as_view(), name='semester_add'),

    ]