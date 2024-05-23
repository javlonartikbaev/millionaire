from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Todos import views

# router = DefaultRouter()
# router.register(r'todos', views.TodoViewSet)


urlpatterns = [
    path('api/', views.QuestionViewSet.as_view()),
]
