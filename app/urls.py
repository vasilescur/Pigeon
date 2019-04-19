from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view()),
    # path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/')),
    path('accounts/profile/', views.redirect_index, name='redirect_index'),

    path('create/', views.create, name='create'),
    path('article/create/', views.create_article, name='create_article'),

    path('drafts/', views.drafts, name='drafts'),

    path('edit/', views.edit, name='edit'),
    path('article/', views.article, name='article'),

    path('article/newtext/', views.article_newtext, name='article_newtext'),
]
