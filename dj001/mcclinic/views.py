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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main_page(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'main/main_page.html', {'page': page,'posts': posts})

def post_list(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'main/post_list.html', {'page': page,'posts': posts})    


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


#doctors


def doctors(request):
    return render(request, 'main/doctors.html', {})

#doctor_page

def doctor_page(request):
    return render(request, 'main/doctor_page.html', {})

#contacts

def contacts(request):
    return render(request, 'main/contacts.html', {})

#docsl

def docsl(request):
    return render(request, 'main/docsl.html', {})

#insurance

def insurance(request):
    return render(request, 'main/insurance.html', {})

#job

def job(request):
    return render(request, 'main/job.html', {})

#promo

def promo(request):
    return render(request, 'main/promo.html', {})

#services

def services(request):
    return render(request, 'main/services.html', {})

#analyzes

def analyzes(request):
    return render(request, 'main/analyzes.html', {})

#analyzes_price

"""
def analyzes_price(request):
    object_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    paginator = Paginator(object_list, 10)  # 10 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request, 'main/allclinic.html', {'page': page,'posts': posts})    
"""





