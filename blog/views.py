from django.shortcuts import render, get_object_or_404, redirect  
from django.utils import timezone    # get_object_or_404: object를 가져오고 없으면 404 에러를 띄우라는 내용의 함수
from .models import Blog


# Create your views here.
def home(request):
    blogs = Blog.objects  # 모델로부터 전달받은 '객체목록'을 'queryset'이라고 부른다
                          # 이러한 'queryset'들을 처리해주는 방법을 메소드라고 한다
    return render(request, 'blog/home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)  # 모델명, 불러올 blog 게시글의 id
                                                       # pk: 객체들을 구분할 수 있는 key(urls.py와 변수명이 다르면 오류)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def write(request):
    return render(request, 'blog/write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()  # queryset method(ex) object.delete())
    return redirect('/blog/' + str(blog.id))  # redirect: 요청을 처리하고 보여주는 페이지(요청 들어오면 저쪽 url로 보내버려)
