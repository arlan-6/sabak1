from django.shortcuts import render, get_object_or_404
from .models import Post


def home_page(request):
    return render(request, "./home.html")


def shop_page(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "./shop.html", context)


def item_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {"post": post}
    return render(request, "item.html", context=context)
