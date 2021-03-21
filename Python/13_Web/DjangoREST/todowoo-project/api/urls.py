from django.urls import path
from . import views


urlpatterns = [
    # ToDos
    path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoComplete.as_view()),
    path('todos/completed', views.TodoCompletedList.as_view()),

    # Auth
    path('signup', views.signup),
    path('login', views.login),
]
