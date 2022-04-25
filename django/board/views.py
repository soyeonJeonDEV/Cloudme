from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostModelForm, PostForm

def index(request):
    # 게시물 목록 출력
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)

def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

def answer_create(request, postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content=request.POST.get('content'), date=timezone.now())
    return redirect('board:detail', postId=postId)
#Create your views here.

def addpostmove(request):

    return render(request, 'board/addpost.html')

    
# 글등록(Form) 사용
@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # 검증을 통과한 입력 데이터
            print(form.cleaned_data)
            clean_data_dict = form.cleaned_data
            # create() 함수가 호출되면 등록처리가 이루어진다.
            post = Post.objects.create(
                writer=request.user,
                title = clean_data_dict['title'],
                content=clean_data_dict['content'],
                date=timezone.now()
            )
            postList = Post.objects.order_by('-date')
            context = {'postList': postList}
            return redirect('/', context)


@login_required
def post_new_modelform(request):
    if request.method == 'POST':
        # 등록을 요청하는 경우
        post_form = PostModelForm(request.POST)
        # 검증로직을 통과하면
        if post_form.is_valid():
            # form 객체의 save() 호출하면 Model 객체가 생성되어진다.
            post = post_form.save(commit=False)
            # 로그인된 username을 작성자(author)필드에 저장
            post.writer = request.user
            # 현재날짜시간을 게시일자(published_date) 필드에 저장
            post.date = timezone.now()
            # post 객체가 저장되면서 insert 처리가 되어진다.
            post.save()
            # 등록 후에 상세페이지로 리다이렉션 처리하기

            postList = Post.objects.order_by('-date')
            context = {'postList': postList}
            return redirect('/board', context)

# 글수정(ModelForm) 사용
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            # form 객체의 save() 호출하면 Model 객체가 생성되어진다.
            post = form.save(commit=False)
            # 로그인된 username을 작성자(author)필드에 저장
            post.writer = request.user
            # 현재날짜시간을 게시일자(published_date) 필드에 저장
            post.date = timezone.now()
            # post 객체가 저장되면서 insert 처리가 되어진다.
            post.save()
            # 등록 후에 상세페이지로 리다이렉션 처리하기
            post = Post.objects.get(id=pk)
            context = {'post': post}
            return redirect('board:detail', pk)

# 글수정(ModelForm) 사용
@login_required
def post_edit_form(request, pk):
    b=Post.objects.get(id=pk)
    data = {"post":b}
    return render(request, 'board/editpost.html',data)

# 글삭제
@login_required
def post_remove(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('/board')
