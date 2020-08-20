from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required


def blog(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'blog/blog.html', context)


def article_detail(request, slug):
    articles = Article.objects.get(slug=slug)
    context = {
        "articles": articles,
    }
    return render(request, 'blog/article_detail.html', context)