from posixpath import basename
from django.urls import path, include
from rest_framework import routers
from . import views


# router = routers.DefaultRouter()
# router.register('projects', views.ProjectViewSet, basename='projects')


# urlpatterns = [
#     path ('', include(router.urls))
# ]

urlpatterns = [
    path ('project/', views.ProjectView.as_view()),
    path ('project/<int:pk>/', views.ProjectCrudView.as_view())

 ]