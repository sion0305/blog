from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    blogList = Blog.objects #쿼리셋 #메소드
    return render(request, 'home.html', {'blogs': blogList})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)#이용자가 원하는 몇번 객체
    
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()#블로그 작성시 시간/import필요
    blog.save() #객체.delete()/DB에서 삭제
    return redirect('/blog/'+str(blog.id))