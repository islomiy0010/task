from django.urls import path
from .views import *


urlpatterns=[
    path('',home,name='home-page'),
    path('signup/',signup,name='signup-page'),
    path('login/',loginForm,name='login-page'),
    path('logout/',logout_view,name='logout-page'),
    path('task_delete/<int:pk>',task_delete,name='task-delete-page'),
    path('task_edit/<int:pk>',task_edit,name='task-edit-page'),
]