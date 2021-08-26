# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
#загрузка для админки файлов
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#вывод модуля для работы с пагинацией (постраничный вывод новостей)
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main_page(request):
    return render(request, 'main/main_page.html', {})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'main/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/post_edit.html', {'form': form})


#загрузка для админки файлов

urlpatterns = [
    path('',  include('mcclinic.urls')),
    path('admin/', admin.site.urls),
]
 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#вывод модуля для работы с пагинацией (постраничный вывод новостей)
 
def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)
 
    context = {
        "postLists": postLists,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "main/post_lists.html", context)





