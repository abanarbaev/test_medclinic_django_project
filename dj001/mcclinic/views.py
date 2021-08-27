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
#Paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template import RequestContext


def main_page(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'main/main_page.html', {'posts': posts})


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


#Paginator

def news(request):
    '''Show all news'''
    posts_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(posts_list, 8)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    vars = dict(
        posts=posts,
        )
    return render('news.html', vars, context_instance=RequestContext(request))


