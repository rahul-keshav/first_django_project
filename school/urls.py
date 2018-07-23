from django.urls import path

from . import views

app_name = 'school'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/class/', views.IndexView.as_view(), name='class'),
    path('<int:pk>/subject/', views.IndexView.as_view(), name='subject'),

    path('add/', views.SchoolCreate.as_view(), name='school_add'),
    ]