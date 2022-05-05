from . import views
from django.urls import path, include
from rest_framework import routers





urlpatterns = [
    path ('cohort/', views.CohortView.as_view()),
    path ('cohort/<int:pk>/', views.CohortCrudView.as_view()),
    path ('native/', views.NativeView.as_view()),
    path ('native/<int:pk>/', views.NativeCrudView.as_view())

 ]





# router = routers.DefaultRouter()
# router.register(r'natives', views.NativeViewSet, basename='native')
# router.register('cohort', views.CohortViewSet, basename='cohort')

# urlpatterns = [
#     path ('', include(router.urls))
# ]



# urlpatterns = [
#     path ('native/', views.NativeView.as_view()),
#     path ('cohort/', views.CohortView.as_view())
# ]