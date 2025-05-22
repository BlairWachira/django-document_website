from django.urls import path
from. import views

urlpatterns = [
    path('', views.sign_user, name='sign'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search/', views.search_results, name='search_results'),
]