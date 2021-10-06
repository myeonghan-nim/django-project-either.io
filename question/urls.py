from django.urls import path

from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/detail/', views.detail, name='detail'),

    path('create/', views.create, name='create'),
    path('<int:question_id>/update/', views.update, name='update'),
    path('<int:question_id>/delete/', views.delete, name='delete'),

    path('<int:question_id>/choice/<int:select>/create/',
         views.create_choice, name='create_choice'),
    path('<int:question_id>/choice/<int:choice_id>/delete/',
         views.delete_choice, name='delete_choice'),
]
