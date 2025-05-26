from django.shortcuts import render, get_object_or_404
from .models import Categories, Posts

def categories(request):
    categories = Categories.objects.order_by('title')
    return render(request, 'blog/categories.html', {'categories': categories})

def categories_detail_view(request, category_pk):
    category = get_object_or_404(Categories, pk=category_pk)
    posts = Posts.objects.filter(category=category).order_by('title')  # Фильтр по категории
    return render(request, 'blog/category_view.html', {'posts': posts, 'category': category})

def posts_detail_view(request, category_pk, post_pk):
    post = get_object_or_404(Posts, pk=post_pk, category_id=category_pk)
    return render(request, 'blog/post_view.html', {'post': post})