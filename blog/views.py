from django.shortcuts import render, get_object_or_404, redirect  
from django.utils import timezone    # get_object_or_404: object를 가져오고 없으면 404 에러를 띄우라는 내용의 함수
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogPost


# Create your views here.
def home(request):
    blogs = Blog.objects  # 모델로부터 전달받은 '객체목록'을 'queryset'이라고 부른다
                          # 이러한 'queryset'들을 처리해주는 방법을 메소드라고 한다

    blog_list = Blog.objects.all()  # 블로그 모든 글
    paginator = Paginator(blog_list, 3)  # 블로그  객체 3개를 한 페이지로 자르기
    page = request.GET.get('page')  # request 된 페이지가 뭔지를 알아낸다(request 페이지를 변수에 담는다)
    posts = paginator.get_page(page)  # request 된 페이지를 얻어온다

    return render(request, 'blog/home.html', {'blogs': blogs, 'posts': posts})

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
    return redirect('/blog/' + str(blog.id))  # redirect: 요청을 처리하고 보여주는 페이지(요청 들어오면 저쪽 url로 보내버려) # url is string

def blogpost(request):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # commit=False: 저장하지 않고 form 데이터만 가져온다
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    
    else:  # GET
        form = BlogPost()
        return render(request, 'write.html', {'form': form})