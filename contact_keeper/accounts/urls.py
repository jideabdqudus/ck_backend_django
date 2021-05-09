from django.urls import path, include
from .views import LoginViews, RegisterViews, UserViews
from knox import views as knox_views

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/register', RegisterViews.as_view()),
    path('api/auth/login', LoginViews.as_view()),
    path('api/auth/user', UserViews.as_view()),
    path('api/auth/logout', knox_views.LogoutView.as_view(), name = 'knox_logout'),
]