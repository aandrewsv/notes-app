from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/<str:pk>/', views.handleNote, name="note"),
    path('signup/', views.signUp, name="signup"),
    path('signin/', views.signIn, name="signin"),
    path('signout/', views.signOut, name="signout"),
    path('user/', views.userView, name="userview"),
]
