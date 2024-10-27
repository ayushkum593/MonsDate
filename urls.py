# dating_app/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet

#router = DefaultRouter()
#router.register(r'profiles', UserProfileViewSet, basename='userprofile')


urlpatterns = [
    #path('', include(router.urls)),
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('social/', include('social_django.urls', namespace='social')),
    path('login/auth0/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]