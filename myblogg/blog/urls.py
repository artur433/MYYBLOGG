from django.urls import path
from . import views

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_pk>/', views.categories_detail_view, name='categories-detail'),
    path('<int:category_pk>/post/<int:post_pk>/', views.posts_detail_view, name='posts-detail'),
]
