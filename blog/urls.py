from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.blog, name="blog-home"),
    path('<slug:slug>/', views.article_detail, name="blog-detail"),
]