from django.urls import path
from . import views

app_name = 'vs'

urlpatterns = [
    path('', views.index, name='index'),
    path('lucky/', views.lucky, name='lucky'),
    path('<int:id>/detail/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:id>/update/', views.update, name='update'),

    path('<int:id>/delete/', views.delete, name='delete'),

    path('<int:id>/choice/<int:select>/', views.choice, name='choice'),
    
    path('<int:q_id>/<int:c_id>/choice-delete/', views.choice_delete, name='choice-delete'),
]
